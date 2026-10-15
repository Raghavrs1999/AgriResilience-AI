# AgriResilience AI — API Contracts & Data Models
## Complete REST API Schemas, Firestore Collections, and BigQuery Analytics

> **Version**: 1.0.0-PROD  
> **Server Base URL**: `https://agriresilience-backend-xyz.a.run.app` (Google Cloud Run)  
> **Protocol**: HTTPS / JSON & Multipart-Form  

---

### 1. REST API Endpoint Specifications

---

#### Endpoint 1: Submit Multimodal Consultation
- **Route**: `POST /api/v1/diagnose`
- **Content-Type**: `multipart/form-data`
- **Request Parameters**:
  | Field | Type | Required | Description |
  | :--- | :--- | :---: | :--- |
  | `leaf_image` | Binary File (JPEG/PNG) | Yes | Macro image of affected crop leaf or stem. Max size: 10MB. |
  | `voice_note` | Binary File (WebM/WAV) | No | Optional spoken audio recording of farmer describing symptoms. |
  | `latitude` | Float | Yes | GPS latitude of the farm parcel (e.g., `19.7515`). |
  | `longitude` | Float | Yes | GPS longitude of the farm parcel (e.g., `75.7139`). |
  | `farmer_id` | String | No | Unique identifier for registered farmer or session ID. |
  | `language_hint` | String | No | Optional language code hint (e.g., `mr-IN`, `hi-IN`, `id-ID`). |

- **Response Body (200 OK)**:
```json
{
  "consultation_id": "c78f912e-4b2a-41d6-8419-f9a2e379b182",
  "timestamp": "2026-10-12T14:30:00Z",
  "crop_info": {
    "crop_name": "Cotton",
    "botanical_name": "Gossypium hirsutum",
    "confidence": 0.985
  },
  "pathology_diagnosis": {
    "disease_name": "Bacterial Blight (Angular Leaf Spot)",
    "causative_pathogen": "Xanthomonas citri pv. malvacearum",
    "pathogen_type": "BACTERIAL",
    "confidence": 0.942,
    "severity_percentage": 38.5,
    "severity_level": "MODERATE_TO_HIGH",
    "symptoms_identified": [
      "Water-soaked angular leaf spots bounded by veins",
      "Chlorotic yellow halos surrounding necrotic lesion centers",
      "Petiole lesion spreading to vascular branch"
    ]
  },
  "geospatial_telemetry": {
    "coordinates": { "lat": 19.7515, "lng": 75.7139 },
    "satellite_source": "COPERNICUS/S2_SR",
    "ndvi_vegetation_index": 0.412,
    "ndvi_status": "VEGETATION_STRESSED",
    "ndwi_moisture_index": 0.285,
    "soil_moisture_status": "SATURATED_MOIST",
    "precipitation_forecast_next_4h_mm": 16.5,
    "rain_washoff_risk": "HIGH",
    "spraying_permitted_now": false,
    "recommended_spray_window_start": "2026-10-13T06:30:00Z",
    "hours_until_safe_spray": 16
  },
  "prescription": {
    "primary_mode": "ORGANIC_BIOPESTICIDE",
    "spray_warning_badge": "HALT: Rain expected in 3 hours. Do not spray today.",
    "treatment_name": "Neem Seed Kernel Extract (5%) + Copper Oxychloride Backup",
    "steps": [
      {
        "step_number": 1,
        "title": "Wait for Dry Weather Window",
        "instruction": "Do not spray immediately. Heavy rainfall will wash away the mixture. Spray tomorrow morning between 6:30 AM and 8:30 AM."
      },
      {
        "step_number": 2,
        "title": "Prepare Organic Bio-Wash",
        "instruction": "Crush 500g of dry neem seeds. Soak overnight in 10 liters of clean water. Filter using a fine cotton cloth and add 20g of soap flakes."
      },
      {
        "step_number": 3,
        "title": "Application Technique",
        "instruction": "Spray thoroughly on the undersides of the cotton leaves where bacterial colonies reside."
      }
    ],
    "estimated_cost_inr": 45.0,
    "commercial_chemical_alternative": {
      "product_name": "Copper Oxychloride 50% WP + Streptocycline 100ppm",
      "dosage": "2.5g Copper Oxychloride + 0.1g Streptocycline per liter of water",
      "estimated_cost_inr": 480.0,
      "withholding_period_days": 14
    }
  },
  "audio_prescription": {
    "language_code": "mr-IN",
    "dialect": "Marathi",
    "audio_stream_url": "https://storage.googleapis.com/agriresilience-audio/prescriptions/c78f912e.mp3",
    "duration_seconds": 38.4
  },
  "epidemiological_alert": {
    "nearby_cluster_detected": true,
    "distance_km": 3.2,
    "farms_affected_in_radius": 5,
    "alert_message": "Warning: Bacterial Blight detected in 5 neighboring cotton plots within 4 km. Alert your village cooperative."
  }
}
```

---

#### Endpoint 2: Fetch Hyperlocal Geospatial Indices
- **Route**: `GET /api/v1/geospatial/indices?lat=19.7515&lng=75.7139`
- **Response Body (200 OK)**:
```json
{
  "latitude": 19.7515,
  "longitude": 75.7139,
  "satellite_pass_date": "2026-10-10",
  "indices": {
    "ndvi": 0.412,
    "ndwi": 0.285,
    "surface_soil_moisture_m3m3": 0.32
  },
  "weather_72h_forecast": [
    { "timestamp": "2026-10-12T15:00:00Z", "rain_prob": 0.85, "rain_mm": 12.0 },
    { "timestamp": "2026-10-12T18:00:00Z", "rain_prob": 0.70, "rain_mm": 4.5 },
    { "timestamp": "2026-10-13T06:00:00Z", "rain_prob": 0.10, "rain_mm": 0.0 }
  ]
}
```

---

#### Endpoint 3: Fetch Regional Outbreak Radar
- **Route**: `GET /api/v1/outbreaks/radar?lat=19.7515&lng=75.7139&radius_km=15`
- **Response Body (200 OK)**:
```json
{
  "query_center": { "lat": 19.7515, "lng": 75.7139 },
  "radius_km": 15.0,
  "total_active_clusters": 2,
  "clusters": [
    {
      "cluster_id": "clust_cotton_blight_01",
      "disease_name": "Bacterial Blight",
      "crop": "Cotton",
      "center_lat": 19.7420,
      "center_lng": 75.7280,
      "incident_count": 8,
      "severity_distribution": { "mild": 2, "moderate": 5, "severe": 1 },
      "first_reported_at": "2026-10-09T08:00:00Z",
      "last_reported_at": "2026-10-12T11:20:00Z"
    }
  ]
}
```

---

### 2. Google Cloud Firestore NoSQL Database Schema

```
DATABASE: (default)
│
├── COLLECTION: farmers
│   └── DOCUMENT: {farmer_id}
│       ├── phone_number: String ("+919822012345")
│       ├── name: String ("Tukaram Shinde")
│       ├── village: String ("Jalna")
│       ├── district: String ("Aurangabad")
│       ├── state: String ("Maharashtra")
│       ├── country: String ("India")
│       ├── preferred_language: String ("mr-IN")
│       ├── total_acreage: Number (2.5)
│       └── created_at: Timestamp
│
├── COLLECTION: consultations
│   └── DOCUMENT: {consultation_id}
│       ├── farmer_id: String ("farmer_102")
│       ├── timestamp: Timestamp
│       ├── geo_point: GeoPoint (19.7515, 75.7139)
│       ├── geohash: String ("te7ug2")
│       ├── crop_name: String ("Cotton")
│       ├── disease_name: String ("Bacterial Blight")
│       ├── severity_percentage: Number (38.5)
│       ├── ndvi_index: Number (0.412)
│       ├── rain_washoff_flag: Boolean (true)
│       ├── raw_image_gcs_url: String ("gs://agriresilience-images/raw/c78f912e.jpg")
│       ├── raw_audio_gcs_url: String ("gs://agriresilience-audio/raw/c78f912e.webm")
│       ├── prescription_audio_gcs_url: String ("gs://agriresilience-audio/prescriptions/c78f912e.mp3")
│       └── status: String ("COMPLETED")
│
└── COLLECTION: outbreak_clusters
    └── DOCUMENT: {cluster_id}
        ├── disease_name: String ("Bacterial Blight")
        ├── crop: String ("Cotton")
        ├── geohash_prefix: String ("te7u")
        ├── incident_count: Number (8)
        ├── center_point: GeoPoint (19.7420, 75.7280)
        ├── is_active: Boolean (true)
        └── updated_at: Timestamp
```

---

### 3. Google BigQuery Epidemiological Analytics Schema

- **Dataset**: `agriresilience_analytics`
- **Table**: `daily_blight_telemetry`

```sql
CREATE TABLE `agriresilience_analytics.daily_blight_telemetry` (
  consultation_id STRING NOT NULL,
  consultation_time TIMESTAMP NOT NULL,
  country_code STRING,
  state_region STRING,
  crop_type STRING,
  pathogen_name STRING,
  severity_score FLOAT64,
  ndvi_index FLOAT64,
  ndwi_moisture_index FLOAT64,
  precipitation_4h_mm FLOAT64,
  washoff_prevented_flag BOOL,
  farmer_language STRING,
  estimated_cost_saved_usd FLOAT64
)
PARTITION BY DATE(consultation_time)
CLUSTER BY crop_type, pathogen_name, state_region;
```

---
*Next Document*: MVP Implementation Plan, Demo Scenarios, and Video Script in [`05_hackathon_mvp_implementation_plan.md`](file:///d:/ai_builder/agri_resilience_docs/05_hackathon_mvp_implementation_plan.md).
