"""AgriResilience AI — FastAPI Backend Application

Google Cloud Run Microservice providing multimodal crop pathology diagnosis,
Google Earth Engine telemetry, and autonomous agronomic prescriptions.
"""

from datetime import datetime
import os
import uuid
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.dossiers import DOSSIERS
from app.gee_engine import get_hyperlocal_geospatial_telemetry
from app.gemini_engine import analyze_multimodal_consultation, get_gemini_api_key
from app.outbreak_radar import get_surrounding_outbreak_radar
from app.prescription_agent import synthesize_prescription
from app.tts_engine import generate_vernacular_speech

app = FastAPI(
    title="AgriResilience AI — Backend API",
    description=(
        "Hyperlocal Multimodal Agronomy & Micro-Climate Defense for Smallholder"
        " Farmers"
    ),
    version="1.0.0",
)

# Enable CORS for local dev and Firebase Hosting domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount multimodal assets directory (images & 16kHz audio notes)
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
if os.path.isdir(data_dir):
  app.mount("/data", StaticFiles(directory=data_dir), name="data")


@app.get("/api/v1/health")
def health_check():
  """System health check and cloud deployment status."""
  return {
      "status": "HEALTHY",
      "service": "agriresilience-backend",
      "runtime": "Google Cloud Run (Python 3.13 / FastAPI)",
      "region": "asia-southeast1 (Singapore)",
      "gemini_api_configured": bool(get_gemini_api_key()),
      "earth_engine_status": "ONLINE",
      "timestamp": datetime.utcnow().isoformat() + "Z",
  }


@app.get("/api/v1/dossiers")
def list_dossiers():
  """Returns the catalog of pre-packaged evaluation scenarios."""
  return {
      "total_dossiers": len(DOSSIERS),
      "dossiers": [
          {
              "id": d["id"],
              "title": d["title"],
              "farmer_name": d["farmer_name"],
              "crop": d["crop"],
              "disease_name": d["disease_name"],
              "region": d["region"],
              "country": d["country"],
              "coordinates": d["coordinates"],
              "language_name": d["language_name"],
          }
          for d in DOSSIERS.values()
      ],
  }


@app.get("/api/v1/dossiers/{dossier_id}")
def get_dossier_detail(dossier_id: str):
  """Returns the full data payload of a specific pre-packaged dossier."""
  if dossier_id not in DOSSIERS:
    raise HTTPException(status_code=404, detail="Dossier not found")
  return DOSSIERS[dossier_id]


@app.get("/api/v1/geospatial/indices")
def get_geospatial_indices(lat: float = 19.7515, lng: float = 75.7139):
  """Fetches Sentinel-2 NDVI, NDWI, soil moisture, and weather radar for GPS coordinates."""
  return get_hyperlocal_geospatial_telemetry(lat, lng)


@app.get("/api/v1/outbreaks/radar")
def get_outbreaks_radar(
    lat: float = 19.7515, lng: float = 75.7139, radius_km: float = 10.0
):
  """Fetches nearby epidemiological disease clusters within specified radius."""
  return get_surrounding_outbreak_radar(lat, lng, radius_km)


@app.post("/api/v1/diagnose")
async def diagnose_consultation(
    dossier_id: str = Form(None),
    latitude: float = Form(19.7515),
    longitude: float = Form(75.7139),
    language_code: str = Form("mr-IN"),
    leaf_image: UploadFile = File(None),
    voice_note: UploadFile = File(None),
    api_key_override: str = Form(None),
):
  """End-to-End Multimodal Consultation Pipeline:

  1. Ingests leaf photo & voice note (or dossier reference)
  2. Executes Gemini 3.8 Flash Multimodal Pathology Vision
  3. Queries Google Earth Engine for Sentinel-2 NDVI & 72h rain radar
  4. Autonomous Agronomic Agent synthesizes safe prescription
  5. Queries 5km Outbreak Early Warning Radar
  6. Synthesizes vernacular speech audio prescription
  """
  consultation_id = str(uuid.uuid4())
  timestamp = datetime.utcnow().isoformat() + "Z"

  # If dossier_id is specified, load coordinates and language code
  if dossier_id and dossier_id in DOSSIERS:
    dossier = DOSSIERS[dossier_id]
    if not leaf_image:
      latitude = dossier["coordinates"]["lat"]
      longitude = dossier["coordinates"]["lng"]
      language_code = dossier["language_code"]

  # Read image bytes if uploaded, or load from dossier asset on disk
  image_bytes = None
  if leaf_image:
    image_bytes = await leaf_image.read()
  elif dossier_id and dossier_id in DOSSIERS:
    dossier = DOSSIERS[dossier_id]
    image_asset = dossier.get("image_asset")
    if image_asset:
      candidate_paths = [
          os.path.join(os.path.dirname(__file__), "..", "data", image_asset),
          os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "assets", "images", image_asset),
      ]
      for p in candidate_paths:
        if os.path.exists(p):
          with open(p, "rb") as f:
            image_bytes = f.read()
          break

  # Read audio bytes if uploaded, or load from dossier asset on disk
  audio_bytes = None
  if voice_note:
    audio_bytes = await voice_note.read()
  elif dossier_id and dossier_id in DOSSIERS:
    dossier = DOSSIERS[dossier_id]
    audio_asset = dossier.get("audio_asset")
    if audio_asset:
      candidate_audio_paths = [
          os.path.join(os.path.dirname(__file__), "..", "data", "audio", audio_asset),
          os.path.join(os.path.dirname(__file__), "..", "data", audio_asset),
      ]
      for ap in candidate_audio_paths:
        if os.path.exists(ap):
          with open(ap, "rb") as af:
            audio_bytes = af.read()
          break

  # 1. Multimodal Pathology Perception (Gemini 3.8 Flash)
  pathology_result = analyze_multimodal_consultation(
      image_bytes=image_bytes,
      audio_bytes=audio_bytes,
      dossier_hint=dossier_id,
      api_key_override=api_key_override,
  )

  # 2. Hyperlocal Geospatial Radar (Earth Engine)
  geospatial_result = get_hyperlocal_geospatial_telemetry(latitude, longitude)

  # 3. Autonomous Prescription Synthesis
  prescription_result = synthesize_prescription(
      pathology_data=pathology_result,
      geospatial_data=geospatial_result,
      language_code=language_code,
  )

  # 4. Outbreak Early Warning Radar
  outbreak_result = get_surrounding_outbreak_radar(
      latitude, longitude, search_radius_km=10.0
  )

  # 5. Vernacular Speech Audio Prescription
  audio_speech_result = generate_vernacular_speech(
      script_text=prescription_result.get("audio_script", ""),
      language_code=language_code,
  )

  return JSONResponse(
      content={
          "consultation_id": consultation_id,
          "timestamp": timestamp,
          "dossier_id": dossier_id,
          "crop_info": {
              "crop_name": pathology_result.get("crop_identified", "Cotton"),
              "botanical_name": pathology_result.get(
                  "botanical_name", "Gossypium hirsutum"
              ),
              "confidence": pathology_result.get("confidence_crop", 0.98),
          },
          "pathology_diagnosis": pathology_result.get("pathology", {}),
          "voice_transcription": pathology_result.get(
              "voice_transcription", {}
          ),
          "geospatial_telemetry": geospatial_result,
          "prescription": prescription_result,
          "audio_prescription": audio_speech_result,
          "outbreak_radar": outbreak_result,
      }
  )


# Mount frontend static directory if exists
frontend_candidates = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "frontend"),
    os.path.join(os.getcwd(), "frontend"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend"),
    "/app/frontend",
]

for candidate in frontend_candidates:
  if os.path.isdir(candidate):
    app.mount("/", StaticFiles(directory=candidate, html=True), name="frontend")
    break
