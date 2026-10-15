"""AgriResilience AI — Synthetic Dataset Exporter

Exports the complete 9-dossier benchmark into standalone JSON and CSV files
in backend/data/ for evaluation, data science inspection, and hackathon judging.
"""

import csv
import json
import os
import sys

# Add backend directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.dossiers import DOSSIERS

OUTPUT_DIR = r"d:\ai_builder\backend\data"
JSON_OUT = os.path.join(OUTPUT_DIR, "synthetic_evaluation_benchmark.json")
CSV_OUT = os.path.join(OUTPUT_DIR, "synthetic_evaluation_matrix.csv")

def export_data():
    # 1. Export Clean JSON Benchmark
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(DOSSIERS, f, indent=2, ensure_ascii=False)
    print(f"[OK] Exported JSON Benchmark -> {JSON_OUT}")

    # 2. Export Tabular CSV Matrix
    fieldnames = [
        "dossier_id", "title", "crop", "botanical_name", "country", "region", "village",
        "latitude", "longitude", "language_code", "language_name",
        "disease_name", "causative_pathogen", "pathogen_type", "severity_percentage",
        "disease_stage", "ndvi", "ndwi", "soil_moisture_m3m3", "precipitation_next_4h_mm",
        "rain_probability_4h", "action_code", "wash_off_risk", "treatment_mode",
        "treatment_name", "cost_inr", "dealer_chemical_cost_inr", "net_savings_inr",
        "image_asset", "audio_asset"
    ]

    rows = []
    for d_id, d in DOSSIERS.items():
        coords = d.get("coordinates", {})
        sat = d.get("satellite_telemetry", {})
        rx = d.get("prescription", {})
        rows.append({
            "dossier_id": d.get("id"),
            "title": d.get("title"),
            "crop": d.get("crop"),
            "botanical_name": d.get("botanical_name"),
            "country": d.get("country"),
            "region": d.get("region"),
            "village": d.get("village"),
            "latitude": coords.get("lat"),
            "longitude": coords.get("lng"),
            "language_code": d.get("language_code"),
            "language_name": d.get("language_name"),
            "disease_name": d.get("disease_name"),
            "causative_pathogen": d.get("causative_pathogen"),
            "pathogen_type": d.get("pathogen_type"),
            "severity_percentage": d.get("severity_percentage"),
            "disease_stage": d.get("disease_stage"),
            "ndvi": sat.get("ndvi"),
            "ndwi": sat.get("ndwi"),
            "soil_moisture_m3m3": sat.get("soil_moisture_m3m3"),
            "precipitation_next_4h_mm": sat.get("precipitation_next_4h_mm"),
            "rain_probability_4h": sat.get("rain_probability_4h"),
            "action_code": rx.get("action_code"),
            "wash_off_risk": rx.get("wash_off_risk"),
            "treatment_mode": rx.get("treatment_mode"),
            "treatment_name": rx.get("treatment_name"),
            "cost_inr": rx.get("cost_inr"),
            "dealer_chemical_cost_inr": rx.get("dealer_chemical_cost_inr"),
            "net_savings_inr": rx.get("net_savings_inr"),
            "image_asset": d.get("image_asset"),
            "audio_asset": d.get("audio_asset"),
        })

    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[OK] Exported CSV Matrix -> {CSV_OUT}")

if __name__ == "__main__":
    export_data()
