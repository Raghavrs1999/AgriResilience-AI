# AgriResilience AI — Detailed Feature Specifications
## Exhaustive Algorithmic, Prompt Engineering, and Implementation Guidelines

> **Scope**: Detailed technical requirements, mathematical formulas, prompt schemas, and algorithmic workflows for all six core platform features.

---

### Feature 1: Vernacular Voice & Audio Consultation Engine

#### 1. Description & User Objective
Enables illiterate and semi-literate smallholder farmers to consult the system naturally by speaking in their native dialect into their smartphone microphone, bypassing text keyboards and dropdown menus.

#### 2. Technical Implementation
- **Audio Capture**: Web Audio API records audio as 16kHz mono `.webm` / `.opus` or `.wav`.
- **Direct Multimodal Ingestion in Gemini 1.5 Pro**: Rather than using a pipeline of Whisper ASR $\rightarrow$ English Translation $\rightarrow$ LLM, the raw audio file is passed directly into **Gemini 1.5 Pro's audio input buffer**.
- **Supported Dialects**:
  - *India*: Hindi (including Bhojpuri & Maithili nuances), Marathi, Telugu, Tamil, Bengali, Kannada, Punjabi.
  - *Southeast Asia*: Bahasa Indonesia, Javanese, Tagalog (Filipino), Vietnamese.
- **Audio Processing System Prompt**:
```text
You are an expert native rural agronomist listening to a smallholder farmer's voice note.
Analyze the audio for:
1. Spoken language and regional dialect.
2. Emotional distress level (urgent pest swarm, slow yellowing, routine question).
3. Primary crop mentioned (or inferred).
4. Reported symptoms (wilting, spots, insect borer holes, leaf curl, stunted growth).
5. Cultural agronomic terms used (e.g., 'Tikka rog', 'Mahla', 'Hama Sundep', 'Wereng').

Output a structured JSON object containing:
- detected_dialect (string)
- symptom_transcription_vernacular (string)
- symptom_translation_english (string)
- urgency_rating (enum: LOW, MEDIUM, CRITICAL)
- farmer_stated_duration_days (integer or null)
```

---

### Feature 2: Multimodal Leaf Pathology & Pest Vision Inspector

#### 1. Description & User Objective
Analyzes close-up smartphone photos of diseased leaves, stems, or fruits to classify the exact botanical pathogen, quantify disease severity, and detect micro-spore formations.

#### 2. Computer Vision & Gemini 1.5 Pro Prompt Architecture
The image buffer is passed alongside the structured system prompt:

```json
{
  "model": "gemini-1.5-pro",
  "generation_config": {
    "temperature": 0.1,
    "response_mime_type": "application/json"
  },
  "system_instruction": "You are a Senior Plant Pathologist certified by ICAR and FAO. You are inspecting a field macro photograph of a crop plant leaf. Inspect pixel patterns, lesion geometry, halo rings, necrosis, and spore clusters. Return strictly valid JSON matching the CropPathologySchema."
}
```

#### 3. Structured JSON Output Schema:
```json
{
  "crop_identified": "Gossypium hirsutum (Cotton)",
  "confidence_crop": 0.98,
  "pathology": {
    "primary_diagnosis": "Bacterial Blight (Angular Leaf Spot)",
    "causative_agent": "Xanthomonas citri pv. malvacearum",
    "pathogen_type": "BACTERIAL",
    "confidence_diagnosis": 0.94,
    "disease_stage": "SPORULATING_SPREADING",
    "affected_leaf_area_percentage": 38.5,
    "visual_markers_observed": [
      "Angular, water-soaked lesions bounded by small leaf veins",
      "Reddish-brown necrotic centers with chlorotic yellow halos",
      "Early black-arm lesion initiation on petiole junction"
    ],
    "differential_diagnoses": [
      { "disease": "Alternaria Leaf Spot", "probability": 0.05 },
      { "disease": "Cercospora Leaf Spot", "probability": 0.01 }
    ]
  }
}
```

---

### Feature 3: Hyperlocal Geospatial Micro-Climate Radar (Google Earth Engine)

#### 1. Description & User Objective
Validates whether the visual leaf blight is supported by environmental telemetry (vegetation index, soil moisture, humidity) and calculates safe spray application windows.

#### 2. Earth Engine Python Pipeline (`gee_engine.py`)
The system takes the farmer's GPS coordinates $[Lat, Long]$ and computes:

```python
import ee

ee.Initialize()


def get_field_geospatial_telemetry(lat: float, lon: float, days_lookback: int = 14):
  point = ee.Geometry.Point([lon, lat])
  buffer = point.buffer(100)  # 1-hectare representative boundary

  # 1. Sentinel-2 Surface Reflectance (L2A)
  s2 = (
      ee.ImageCollection('COPERNICUS/S2_SR')
      .filterBounds(buffer)
      .filterDate(
          ee.Date('now').advance(-days_lookback, 'day'), ee.Date('now')
      )
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30))
      .sort('system:time_start', False)
      .first()
  )

  # Calculate NDVI: (NIR - Red) / (NIR + Red) -> Bands B8 & B4
  nir = s2.select('B8')
  red = s2.select('B4')
  ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')

  # Calculate NDWI (Moisture Stress): (NIR - SWIR) / (NIR + SWIR) -> Bands B8 & B11
  swir = s2.select('B11')
  ndwi = nir.subtract(swir).divide(nir.add(swir)).rename('NDWI')

  # Reduce to point values
  stats = (
      ndvi.addBands(ndwi)
      .reduceRegion(reducer=ee.Reducer.mean(), geometry=buffer, scale=10)
      .getInfo()
  )

  # 2. ERA5-Land Precipitation & 2m Temperature (Next 72 Hours Forecast Mock/Live)
  # Computes hourly precipitation accumulation
  return {
      'ndvi_mean': stats.get('NDVI', 0.45),
      'ndwi_moisture_stress': stats.get('NDWI', 0.12),
      'soil_moisture_status': (
          'WATERLOGGED'
          if stats.get('NDWI', 0) > 0.3
          else 'OPTIMAL' if stats.get('NDWI', 0) > 0.1 else 'DROUGHT_STRESSED'
      ),
      'precipitation_next_4h_mm': 18.5,  # Heavy downpour incoming
      'precipitation_next_72h_mm': 42.0,
      'rain_probability_4h': 0.85,
  }
```

---

### Feature 4: Autonomous Agronomic Prescription Engine

#### 1. Multi-Tier Remediation Decision Tree
The agent evaluates the combined vector:
$$\mathbf{V} = [\text{Pathogen}, \text{Severity \%}, \text{NDVI}, \text{Rain Prob}_{4h}]$$

```
                      [ FUSED INPUT EVALUATION ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
   [ Rain Prob (4h) > 60% ]                 [ Rain Prob (4h) ≤ 60% ]
              │                                         │
              ▼                                         ▼
   ⛔ ACTION: HALT SPRAYING!                 [ Check Severity % ]
   Reason: Immediate wash-off                │
   Advisory: Wait for dry window             ├──────────────────────────┐
   Time recommendation: +18 hours            ▼                          ▼
                                    [ Severity < 30% ]         [ Severity ≥ 30% ]
                                             │                          │
                                             ▼                          ▼
                                    TIER 1: BIO / ORGANIC     TIER 2: TARGETED CHEMICAL
                                    • Neem Oil Extract (5%)    • Copper Oxychloride 50% WP
                                    • Sour Buttermilk Spray    • Streptocycline 100ppm
                                    • Cow Urine + Asafoetida   • Withholding Period: 14d
```

#### 2. Structured Actionable Output:
Each prescription contains:
- **Immediate Warning**: Spraying go/no-go badge with exact hours to wait.
- **Recipe Step 1 (Preparation)**: Exact kitchen/village measurements (e.g., *"Take 50ml Neem oil, mix with 10ml liquid soap in 15 liters of water"*).
- **Recipe Step 2 (Application Technique)**: Spray on underside of leaves in early morning or late afternoon.
- **Cost Comparison**: Estimates organic treatment cost (e.g., ₹45) vs. commercial pesticide cost (e.g., ₹650).

---

### Feature 5: Hyperlocal Outbreak Early Warning Radar

#### 1. Epidemiological Clustering Algorithm
When any consultation is confirmed positive for an infectious airborne or waterborne spore (e.g., Rice Blast, Cotton Bollworm):
1. The backend pushes the record to Firestore with a geohash:
   $$\text{Geohash Level 6} \approx 1.2\text{ km} \times 0.6\text{ km}$$
2. The system executes a spatial radius query ($R = 5\text{ km}$):
   $$\text{Distance} = 2R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)}\right)$$
3. If $\ge 3$ neighboring farms confirm identical infection within 72 hours, an **Epidemiological Cluster Alert** triggers on the public map.
4. Surrounding farmers receive proactive notification badges on their PWA: *"Warning: Rice Blast detected in 4 paddies within 3.5 km. Inspect your field's border rows."*

---

### Feature 6: Dialect Audio Prescription Generator

#### 1. Synthesis Pipeline
- The written prescription text is transformed into a natural, conversational script in the farmer’s regional dialect.
- The script is synthesized using Google Cloud Text-to-Speech API with **Neural2** high-fidelity models:
  - Language Code: `mr-IN` (Marathi) or `hi-IN` (Hindi)
  - Audio Encoding: `MP3`
  - Speaking Rate: `0.92` (slightly relaxed cadence for elderly rural listeners)
  - Pitch: `-1.0` (warm, authoritative tone)
- The generated audio is streamed directly to the frontend and rendered alongside an interactive audio waveform visualizer.

---
*Next Document*: Production API Contracts and Data Models in [`04_api_contracts_and_data_models.md`](file:///d:/ai_builder/agri_resilience_docs/04_api_contracts_and_data_models.md).
