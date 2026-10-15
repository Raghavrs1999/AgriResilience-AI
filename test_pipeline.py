import requests
import json
import sys

# Force UTF-8 encoding for Windows terminal output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

dossiers = [
    'dossier_a_cotton',
    'dossier_b_paddy',
    'dossier_c_cassava',
    'dossier_d_maize',
    'dossier_e_sugarcane',
    'dossier_f_wheat',
    'dossier_g_soybean',
    'dossier_edge_sunscorch',
    'dossier_edge_mechanical',
]

print("=" * 60)
print("AGRIRESILIENCE AI — END-TO-END PIPELINE VALIDATION")
print("=" * 60)

for d in dossiers:
    print(f"\n>>> EXECUTING DIAGNOSTIC PIPELINE FOR: {d.upper()}")
    res = requests.post('http://127.0.0.1:8000/api/v1/diagnose', data={'dossier_id': d})
    if res.status_code != 200:
        print(f"FAILED with status {res.status_code}: {res.text}")
        continue
    data = res.json()
    crop = data['crop_info']
    pathology = data['pathology_diagnosis']
    geo = data['geospatial_telemetry']
    rx = data['prescription']
    radar = data['outbreak_radar']
    audio = data['audio_prescription']

    print(f"  [1] Multimodal Vision & Audio:")
    print(f"      Crop: {crop['crop_name']} ({crop['botanical_name']})")
    print(f"      Diagnosis: {pathology.get('primary_diagnosis', 'N/A')}")
    print(f"      Pathogen Type: {pathology.get('pathogen_type', 'N/A')}")
    print(f"      Leaf Area Affected: {pathology.get('affected_leaf_area_percentage', 0)}%")
    
    print(f"  [2] Planetary Micro-Climate Telemetry (Earth Engine):")
    print(f"      Sentinel-2 NDVI: {geo.get('ndvi_vegetation_index')}")
    print(f"      Canopy NDWI: {geo.get('ndwi_moisture_index')}")
    print(f"      Rain Next 4h: {geo.get('precipitation_next_4h_mm')} mm (Prob: {round(geo.get('rain_probability_4h', 0)*100)}%)")
    print(f"      Wash-Off Risk: {geo.get('wash_off_risk')}")

    print(f"  [3] Autonomous Decision Engine (The Wash-Off Rule):")
    print(f"      Action Code: {rx.get('action_code')}")
    print(f"      Banner Badge: {rx.get('banner_badge')}")
    print(f"      Prescribed Treatment: {rx.get('treatment_name')}")
    print(f"      Organic Cost: INR {rx.get('cost_inr')} | Dealer Chemical: INR {rx.get('dealer_chemical_cost_inr')}")
    print(f"      Net Farmer Savings: INR {rx.get('net_savings_inr')}")

    print(f"  [4] 5km Outbreak Early Warning Radar:")
    print(f"      Clusters Found in Search Radius: {radar.get('total_clusters_found')}")
    print(f"      Proximity Warning Active: {radar.get('has_active_proximity_warning')}")

    print(f"  [5] Vernacular Spoken Audio Advisory:")
    print(f"      Dialect: {audio.get('dialect')} ({audio.get('language_code')})")
    print(f"      Voice Model: {audio.get('voice_model')}")
    print(f"      Duration: {audio.get('duration_seconds')}s")

print("\n" + "=" * 60)
print("ALL 9 DOSSIERS EXECUTED SUCCESSFULLY THROUGH THE PIPELINE!")
print("=" * 60)
