"""AgriResilience AI — Hyperlocal Outbreak Early Warning Radar

Calculates Haversine spatial distances, clusters contiguous crop infections,
and broadcasts alerts to neighboring farms within a 5-kilometer radius.
"""

import math
from typing import Any, Dict, List

# Active mock outbreak cluster seeds for testing & demonstration
KNOWN_OUTBREAK_CLUSTERS = [
    {
        "cluster_id": "clust_jalna_cotton_blight",
        "disease_name": "Bacterial Blight",
        "crop": "Cotton",
        "center_lat": 19.8320,
        "center_lng": 75.6800,
        "incident_count": 6,
        "radius_km": 4.2,
        "first_detected": "2026-10-10T08:00:00Z",
        "severity": "CRITICAL",
        "message": (
            "Epidemiological Warning: Bacterial Blight active across 6 cotton"
            " fields in Jalna East cluster. Spores moving with prevailing winds."
        ),
    },
    {
        "cluster_id": "clust_nadia_paddy_blast",
        "disease_name": "Rice Blast",
        "crop": "Paddy Rice",
        "center_lat": 23.4250,
        "center_lng": 88.4720,
        "incident_count": 7,
        "radius_km": 4.8,
        "first_detected": "2026-10-11T09:30:00Z",
        "severity": "EPIDEMIC",
        "message": (
            "Urgent Outbreak Alert: Airborne Rice Blast confirmed in 7 nearby"
            " paddies in Nadia cluster. High humidity favors rapid"
            " sporulation."
        ),
    },
    {
        "cluster_id": "clust_gunungkidul_cassava_whitefly",
        "disease_name": "Cassava Mosaic Disease (CMD)",
        "crop": "Cassava",
        "center_lat": -8.0180,
        "center_lng": 110.6520,
        "incident_count": 3,
        "radius_km": 2.5,
        "first_detected": "2026-10-12T06:00:00Z",
        "severity": "MODERATE",
        "message": (
            "Vector Swarm Alert: Whitefly vector activity spreading CMD across"
            " 3 cassava plots in Gunungkidul sector. Rogue infected stools."
        ),
    },
    {
        "cluster_id": "clust_guntur_maize_fall_armyworm",
        "disease_name": "Turcicum Blight + Fall Armyworm",
        "crop": "Maize",
        "center_lat": 16.2120,
        "center_lng": 80.6150,
        "incident_count": 4,
        "radius_km": 2.5,
        "first_detected": "2026-10-13T10:15:00Z",
        "severity": "CRITICAL",
        "message": (
            "Pest Vector Alert: Fall Armyworm larvae actively defoliating 4"
            " maize plots in Angalakuduru-Tenali cluster. Rain incoming; do not spray."
        ),
    },
    {
        "cluster_id": "clust_thanjavur_sugarcane_redrot",
        "disease_name": "Sugarcane Red Rot",
        "crop": "Sugarcane",
        "center_lat": 10.9180,
        "center_lng": 79.3320,
        "incident_count": 3,
        "radius_km": 2.8,
        "first_detected": "2026-10-14T07:45:00Z",
        "severity": "HIGH",
        "message": (
            "Soil & Water Pathogen Alert: Red Rot (Colletotrichum falcatum)"
            " spreading through Cauvery canal irrigation water in Kumbakonam."
        ),
    },
    {
        "cluster_id": "clust_karnal_wheat_yellow_rust",
        "disease_name": "Yellow / Stripe Rust",
        "crop": "Wheat",
        "center_lat": 29.7350,
        "center_lng": 77.0320,
        "incident_count": 8,
        "radius_km": 4.6,
        "first_detected": "2026-10-14T11:20:00Z",
        "severity": "EPIDEMIC",
        "message": (
            "Airborne Spore Warning: Puccinia striiformis stripe rust spores"
            " moving rapidly across 8 wheat fields with westerly winds in Karnal."
        ),
    },
    {
        "cluster_id": "clust_daklak_soybean_asian_rust",
        "disease_name": "Asian Soybean Rust",
        "crop": "Soybean",
        "center_lat": 12.8750,
        "center_lng": 108.1320,
        "incident_count": 5,
        "radius_km": 3.5,
        "first_detected": "2026-10-15T05:00:00Z",
        "severity": "CRITICAL",
        "message": (
            "Tropical Spore Squall: Asian Soybean Rust confirmed across 5 farms"
            " in Cu M'gar district, Dak Lak. Heavy monsoon downpour imminent."
        ),
    },
]


def haversine_distance_km(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
  """Calculates great-circle distance between two GPS coordinates in kilometers."""
  r = 6371.0  # Earth's radius in km
  phi1 = math.radians(lat1)
  phi2 = math.radians(lat2)
  delta_phi = math.radians(lat2 - lat1)
  delta_lambda = math.radians(lon2 - lon1)

  a = (
      math.sin(delta_phi / 2.0) ** 2
      + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
  )
  c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
  return round(r * c, 2)


def get_surrounding_outbreak_radar(
    lat: float, lng: float, search_radius_km: float = 10.0
) -> Dict[str, Any]:
  """Finds all disease clusters within the search radius of the farm coordinates."""
  matched_clusters: List[Dict[str, Any]] = []

  for cluster in KNOWN_OUTBREAK_CLUSTERS:
    dist = haversine_distance_km(
        lat, lng, cluster["center_lat"], cluster["center_lng"]
    )
    if dist <= search_radius_km:
      cluster_copy = dict(cluster)
      cluster_copy["distance_km"] = dist
      matched_clusters.append(cluster_copy)

  # Check if there is an active cluster within 5km
  nearby_warning = any(c["distance_km"] <= 5.0 for c in matched_clusters)

  return {
      "query_location": {"lat": lat, "lng": lng},
      "search_radius_km": search_radius_km,
      "total_clusters_found": len(matched_clusters),
      "has_active_proximity_warning": nearby_warning,
      "clusters": matched_clusters,
  }
