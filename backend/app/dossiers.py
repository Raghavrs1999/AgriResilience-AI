"""AgriResilience AI — High-Fidelity Pre-Packaged Demo Scenarios (Dossiers)

Provides domain-accurate pathology, coordinates, farmer voice notes,
satellite telemetry, and prescription baselines for hackathon evaluation.
"""

DOSSIERS = {
    "dossier_a_cotton": {
        "id": "dossier_a_cotton",
        "title": "Dossier A: Maharashtra Cotton (Rain Wash-Off Crisis)",
        "farmer_name": "Tukaram Shinde",
        "village": "Jalna",
        "region": "Aurangabad Division, Maharashtra",
        "country": "India",
        "coordinates": {"lat": 19.8250, "lng": 75.6700},
        "crop": "Cotton",
        "botanical_name": "Gossypium hirsutum",
        "language_code": "mr-IN",
        "language_name": "Marathi",
        "image_asset": "cotton_blight.jpg",
        "audio_asset": "cotton_blight_mr_16k.wav",
        "voice_transcript_native": (
            "साहेब, आमच्या कपाशीच्या पानांवर काळे-तांबडे डाग पडले आहेत आणि झाड"
            " सुकत चाललंय. काय फवारणी करू?"
        ),
        "voice_transcript_english": (
            "Sir, blackish-red spots have appeared on our cotton leaves and the"
            " plants are wilting. What should I spray?"
        ),
        "disease_name": "Bacterial Blight (Angular Leaf Spot)",
        "causative_pathogen": "Xanthomonas citri pv. malvacearum",
        "pathogen_type": "BACTERIAL",
        "severity_percentage": 38.5,
        "disease_stage": "ACTIVE_VEGETATIVE_SPREAD",
        "visual_symptoms": [
            "Angular water-soaked leaf lesions strictly bounded by small veins",
            "Necrotic reddish-brown lesion centers with chlorotic yellow halos",
            (
                "Incipient black-arm lesion extending into petiole vascular"
                " tissue"
            ),
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.412,
            "ndvi_status": "MODERATE_CANOPY_STRESS",
            "ndwi": 0.285,
            "soil_moisture_m3m3": 0.34,
            "soil_status": "HIGH_MOISTURE_SATURATION",
            "precipitation_next_4h_mm": 18.5,
            "precipitation_next_72h_mm": 54.0,
            "rain_probability_4h": 0.88,
        },
        "prescription": {
            "action_code": "HALT_SPRAYING",
            "banner_badge": (
                "⛔ HALT: Heavy rain (18mm) expected in 3 hours. Do not spray"
                " today."
            ),
            "wash_off_risk": "CRITICAL",
            "hours_to_wait": 16,
            "recommended_window": "Tomorrow between 6:30 AM and 8:30 AM",
            "treatment_mode": "ORGANIC_BIOPROTECTION_FIRST",
            "treatment_name": (
                "Neem Seed Kernel Extract 5% (NSKE) + Copper Oxychloride Backup"
            ),
            "steps": [
                {
                    "step": 1,
                    "title": "Hold Spray Application",
                    "instruction": (
                        "Immediate spraying will be washed off by incoming"
                        " rainstorm within 3 hours, wasting ₹500 in input costs."
                    ),
                },
                {
                    "step": 2,
                    "title": "Prepare Organic Neem Extract",
                    "instruction": (
                        "Crush 500g dry neem seeds. Soak overnight in 10 liters"
                        " water. Filter through cloth and mix with 20g soap"
                        " flakes."
                    ),
                },
                {
                    "step": 3,
                    "title": "Foliar Spraying Technique",
                    "instruction": (
                        "Spray tomorrow morning thoroughly on leaf undersides"
                        " where Xanthomonas bacteria multiply."
                    ),
                },
            ],
            "cost_inr": 45.0,
            "dealer_chemical_cost_inr": 550.0,
            "net_savings_inr": 505.0,
            "chemical_alternative": {
                "product": (
                    "Copper Oxychloride 50% WP (2.5g/L) + Streptocycline 100ppm"
                    " (0.1g/L)"
                ),
                "withholding_period_days": 14,
            },
        },
        "audio_prescription_script": (
            "नमस्कार तुकारामजी. तुमच्या कपाशीवर जिवाणू करपा म्हणजेच"
            " बॅक्टेरियल ब्लाईट रोगाचा प्रादुर्भाव झाला आहे. अत्यंत महत्त्वाची"
            " सूचना: आज लगेच कोणतीही औषध फवारणी करू नका! सॅटेलाइट रडारनुसार पुढच्या"
            " ३ तासांत जोरदार पाऊस येणार असून औषध वाहून जाईल आणि तुमचे पैसे वाया"
            " जातील. उद्या सकाळी साडेसहा ते साडेआठ दरम्यान पाच टक्के निंबोळी अर्क"
            " पानांच्या खालच्या बाजूने फवारा. यामुळे तुमचे ५०० रुपये वाचतील."
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 5,
            "radius_km": 3.8,
            "message": (
                "Alert: Bacterial Blight confirmed in 5 adjacent cotton farms"
                " in Jalna cluster. Alert your village cooperative."
            ),
        },
    },
    "dossier_b_paddy": {
        "id": "dossier_b_paddy",
        "title": "Dossier B: West Bengal Paddy (Airborne Rice Blast Cluster)",
        "farmer_name": "Debabrata Roy",
        "village": "Nadia District",
        "region": "Gangetic Plain, West Bengal",
        "country": "India",
        "coordinates": {"lat": 23.4180, "lng": 88.4620},
        "crop": "Paddy Rice",
        "botanical_name": "Oryza sativa",
        "language_code": "bn-IN",
        "language_name": "Bengali",
        "image_asset": "rice_blast.jpg",
        "audio_asset": "rice_blast_bn_16k.wav",
        "voice_transcript_native": (
            "ধান গাছের পাতায় নৌকার মতো চোখের দাগ হয়েছে। পুরো মাঠ নষ্ট হয়ে"
            " যাবে মনে হচ্ছে।"
        ),
        "voice_transcript_english": (
            "Spindle-shaped eye spots have formed on the paddy leaves. It looks"
            " like the whole field will be ruined."
        ),
        "disease_name": "Rice Blast (Leaf & Collar Blast)",
        "causative_pathogen": "Magnaporthe oryzae (Pyricularia oryzae)",
        "pathogen_type": "FUNGAL",
        "severity_percentage": 48.0,
        "disease_stage": "EPIDEMIC_SPORULATION",
        "visual_symptoms": [
            (
                "Classic diamond/spindle-shaped lesions with ash-grey centers"
                " and brown margins"
            ),
            "Coalescing lesions leading to leaf blade desiccation and firing",
            (
                "Presence of velvety olive-green conidiophores on lesion"
                " centers"
            ),
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.385,
            "ndvi_status": "SEVERE_CANOPY_CHLOROSIS",
            "ndwi": 0.420,
            "soil_moisture_m3m3": 0.48,
            "soil_status": "PADDY_SUBMERGED_SATURATION",
            "precipitation_next_4h_mm": 0.0,
            "precipitation_next_72h_mm": 2.0,
            "rain_probability_4h": 0.08,
        },
        "prescription": {
            "action_code": "SAFE_TO_SPRAY",
            "banner_badge": (
                "✅ CLEAR WEATHER WINDOW: 48h dry window. Spray immediately."
            ),
            "wash_off_risk": "LOW",
            "hours_to_wait": 0,
            "recommended_window": (
                "Today afternoon (4:00 PM - 6:00 PM) or tomorrow morning"
            ),
            "treatment_mode": "RAPID_BIO_FUNGICIDE_CONTAINMENT",
            "treatment_name": (
                "Pseudomonas fluorescens Bio-Control OR Tricyclazole 75% WP"
            ),
            "steps": [
                {
                    "step": 1,
                    "title": "Confirm Optimal Spray Window",
                    "instruction": (
                        "Satellite radar confirms clear skies with zero rain"
                        " for 48 hours. Fungal spores are actively spreading;"
                        " spray immediately."
                    ),
                },
                {
                    "step": 2,
                    "title": "Bio-Control Foliar Application",
                    "instruction": (
                        "Dissolve Pseudomonas fluorescens (talc formulation) at"
                        " 10g per liter of clean water."
                    ),
                },
                {
                    "step": 3,
                    "title": "Targeted Leaf Canopy Coverage",
                    "instruction": (
                        "Ensure deep spray penetration into lower leaf blades"
                        " and collar nodes before early evening fog."
                    ),
                },
            ],
            "cost_inr": 85.0,
            "dealer_chemical_cost_inr": 720.0,
            "net_savings_inr": 635.0,
            "chemical_alternative": {
                "product": (
                    "Tricyclazole 75% WP (0.6g/L) OR Isoprothiolane 40% EC"
                    " (1.5ml/L)"
                ),
                "withholding_period_days": 21,
            },
        },
        "audio_prescription_script": (
            "নমস্কার দেবব্রতবাবু। আপনার ধানে ব্লাস্ট রোগের লক্ষণ নিশ্চিত"
            " হয়েছে। আবহাওয়া স্যাটেলাইট তথ্য অনুযায়ী আগামী ৪৮ ঘণ্টা বৃষ্টির"
            " কোনো সম্ভাবনা নেই। তাই অবিলম্বে আজ বিকেলেই সিউডোমোনাস ফ্লোরোসেন্স"
            " অথবা ট্রাইসাইক্লাজোল স্প্রে করুন। আশেপাশের ৪টি ধানের জমিতেও ব্লাস্ট"
            " ছড়িয়েছে, তাই সমবায় সমিতির সবাইকে এখনই জমিতে নজরদারি করতে বলুন।"
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 6,
            "radius_km": 4.1,
            "message": (
                "High Alert: Airborne Rice Blast confirmed in 6 nearby paddies"
                " in Nadia cluster. Spores moving northeast."
            ),
        },
    },
    "dossier_c_cassava": {
        "id": "dossier_c_cassava",
        "title": "Dossier C: Central Java Cassava (Viral Stunting Trap)",
        "farmer_name": "Budi Santoso",
        "village": "Gunungkidul",
        "region": "D.I. Yogyakarta",
        "country": "Indonesia",
        "coordinates": {"lat": -8.0120, "lng": 110.6450},
        "crop": "Cassava (Singkong)",
        "botanical_name": "Manihot esculenta",
        "language_code": "id-ID",
        "language_name": "Bahasa Indonesia",
        "image_asset": "cassava_mosaic.jpg",
        "audio_asset": "cassava_cmd_id_16k.wav",
        "voice_transcript_native": (
            "Daun singkong saya menguning keriting dan batangnya kerdil. Ini"
            " kena penyakit apa ya pak?"
        ),
        "voice_transcript_english": (
            "My cassava leaves are yellowing, curling, and the stem is stunted."
            " What sickness is this, sir?"
        ),
        "disease_name": "Cassava Mosaic Disease (CMD)",
        "causative_pathogen": "Cassava Mosaic Geminivirus (Vector: Whitefly)",
        "pathogen_type": "VIRAL",
        "severity_percentage": 55.0,
        "disease_stage": "SYSTEMIC_VIRAL_INFECTION",
        "visual_symptoms": [
            "Severe yellow-green mosaic chlorosis with puckered leaf laminas",
            "Distorted, stunted leaflets with asymmetric leaf margins",
            "General internodal shortening and plant stunting",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.450,
            "ndvi_status": "STUNTED_CANOPY_GROWTH",
            "ndwi": -0.050,
            "soil_moisture_m3m3": 0.18,
            "soil_status": "DROUGHT_STRESSED_KARST_SOIL",
            "precipitation_next_4h_mm": 0.0,
            "precipitation_next_72h_mm": 0.5,
            "rain_probability_4h": 0.02,
        },
        "prescription": {
            "action_code": "HALT_CHEMICALS_ROGUE_PLANTS",
            "banner_badge": (
                "⚠️ VIRAL DISEASE: Do not buy fungicides. Roguing required."
            ),
            "wash_off_risk": "N/A",
            "hours_to_wait": 0,
            "recommended_window": "Immediate mechanical sanitation",
            "treatment_mode": "BIOLOGICAL_VECTOR_CONTROL_AND_SANITATION",
            "treatment_name": (
                "Uproot Infected Stools (Roguing) + Yellow Sticky Traps for"
                " Whitefly"
            ),
            "steps": [
                {
                    "step": 1,
                    "title": "Stop Chemical Spending",
                    "instruction": (
                        "Cassava Mosaic is caused by a virus. Chemical"
                        " fungicides cannot cure it. Do not waste 200,000 IDR"
                        " on dealer sprays."
                    ),
                },
                {
                    "step": 2,
                    "title": "Rogue and Burn Infected Plants",
                    "instruction": (
                        "Immediately dig out severely stunted infected cassava"
                        " plants and burn them outside the field to prevent"
                        " whitefly transmission."
                    ),
                },
                {
                    "step": 3,
                    "title": "Whitefly Vector Management",
                    "instruction": (
                        "Install yellow sticky traps (1 trap every 20 meters)"
                        " to trap Bemisia tabaci whiteflies."
                    ),
                },
            ],
            "cost_inr": 25.0,
            "dealer_chemical_cost_inr": 950.0,
            "net_savings_inr": 925.0,
            "chemical_alternative": {
                "product": (
                    "No curative chemical exists for viral CMD. Manage"
                    " whitefly vectors with Neem spray."
                ),
                "withholding_period_days": 0,
            },
        },
        "audio_prescription_script": (
            "Halo Pak Budi. Tanaman singkong bapak terserang virus mozaik"
            " singkong yang disebarkan oleh kutu kebul. Peringatan penting:"
            " jangan beli obat semprot fungisida kimia karena virus tidak bisa"
            " disembuhkan dengan semprotan biasa! Segera cabut dan musnahkan"
            " batang singkong yang kerdil agar tidak menular ke tanaman lain,"
            " lalu pasang perangkap kuning untuk menangkap kutu kebul. Ini akan"
            " menyelamatkan panen bapak tanpa buang uang ratusan ribu rupiah."
        ),
        "outbreak_alert": {
            "is_cluster": False,
            "nearby_farms_count": 1,
            "radius_km": 1.2,
            "message": (
                "Whitefly vector activity elevated in Gunungkidul sector."
                " Monitor healthy border rows."
            ),
        },
    },
    "dossier_d_maize": {
        "id": "dossier_d_maize",
        "title": "Dossier D: Andhra Pradesh Maize (Fall Armyworm & Rain Crisis)",
        "farmer_name": "Venkat Rao",
        "village": "Angalakuduru (Tenali Rural)",
        "region": "Guntur District, Andhra Pradesh",
        "country": "India",
        "coordinates": {"lat": 16.2050, "lng": 80.6080},
        "crop": "Maize (Corn)",
        "botanical_name": "Zea mays",
        "language_code": "te-IN",
        "language_name": "Telugu",
        "image_asset": "maize_blight_pest.jpg",
        "audio_asset": "maize_blight_te_16k.wav",
        "voice_transcript_native": (
            "అయ్యా, మొక్కజొన్న ఆకులపై పెద్ద మచ్చలు పడ్డాయి, పురుగులు ఆకులను తినేస్తున్నాయి. వెంటనే ఏం మందు కొట్టాలి?"
        ),
        "voice_transcript_english": (
            "Sir, large spots have formed on the maize leaves and caterpillars are devouring them. What medicine should I spray immediately?"
        ),
        "disease_name": "Turcicum Blight + Fall Armyworm",
        "causative_pathogen": "Exserohilum turcicum + Spodoptera frugiperda",
        "pathogen_type": "FUNGAL_INSECT_COMPLEX",
        "severity_percentage": 42.0,
        "disease_stage": "MID_WHORL_FEEDING_AND_BLIGHT",
        "visual_symptoms": [
            "Oblong elliptical tan necrotic lesions bounded by longitudinal leaf veins",
            "Windowpane leaf feeding tears with coarse caterpillar frass in the leaf whorls",
            "Active Spodoptera frugiperda larvae feeding on leaf margins",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.492,
            "ndvi_status": "MODERATE_DEFOLIATION_STRESS",
            "ndwi": 0.120,
            "soil_moisture_m3m3": 0.28,
            "soil_status": "SATURATED_LOAM",
            "precipitation_next_4h_mm": 14.0,
            "precipitation_next_72h_mm": 38.0,
            "rain_probability_4h": 0.78,
        },
        "prescription": {
            "action_code": "HALT_SPRAYING_RAIN_IMMINENT",
            "banner_badge": (
                "⛔ HALT: Heavy rain (14mm) expected in 3 hours. Do not spray chemicals today."
            ),
            "wash_off_risk": "CRITICAL",
            "hours_to_wait": 18,
            "recommended_window": "Tomorrow morning (7:00 AM - 9:00 AM) after convective front passes",
            "treatment_mode": "INTEGRATED_BIO_PEST_AND_BLIGHT_DEFENSE",
            "treatment_name": "Bacillus thuringiensis (Bt) + Trichoderma harzianum Foliar Spray",
            "steps": [
                {
                    "step": 1,
                    "title": "Hold Spraying Operation",
                    "instruction": "Radar shows heavy rainstorm arriving in 3 hours. Spraying now will wash away expensive chemical pesticides.",
                },
                {
                    "step": 2,
                    "title": "Hand Whorl Sand Application",
                    "instruction": "Drop a pinch of dry fine sand mixed with neem seed powder into whorls to physically suffocate active larvae.",
                },
                {
                    "step": 3,
                    "title": "Bio-Spray Application",
                    "instruction": "Spray Bt formulation (2g/L) tomorrow morning directly into the central funnel whorls.",
                },
            ],
            "cost_inr": 60.0,
            "dealer_chemical_cost_inr": 680.0,
            "net_savings_inr": 620.0,
            "chemical_alternative": {
                "product": "Chlorantraniliprole 18.5% SC (0.4ml/L) + Mancozeb 75% WP (2g/L)",
                "withholding_period_days": 14,
            },
        },
        "audio_prescription_script": (
            "నమస్కారం వెంకటరావు గారు. మీ మొక్కజొన్న పైరుపై లద్దెపురుగు మరియు ఆకుమచ్చ తెగులు ఆశించాయి. అత్యవసర హెచ్చరిక: రాబోయే 3 గంటల్లో భారీ వర్షం పడే సూచన ఉంది, కాబట్టి ఈరోజు ఎలాంటి మందులు పిచికారీ చేయవద్దు. రేపు ఉదయం వేప పిండి లేదా జీవ నియంత్రణ మందులు చల్లండి. దీనివల్ల మీ డబ్బు ఆదా అవుతుంది."
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 4,
            "radius_km": 3.2,
            "message": "Warning: Fall Armyworm whorl infestation confirmed across 4 maize plots in Tenali cluster.",
        },
    },
    "dossier_e_sugarcane": {
        "id": "dossier_e_sugarcane",
        "title": "Dossier E: Tamil Nadu Sugarcane (Red Rot Epidemic)",
        "farmer_name": "Murugan Palanisamy",
        "village": "Kumbakonam",
        "region": "Thanjavur Delta, Tamil Nadu",
        "country": "India",
        "coordinates": {"lat": 10.9120, "lng": 79.3250},
        "crop": "Sugarcane",
        "botanical_name": "Saccharum officinarum",
        "language_code": "ta-IN",
        "language_name": "Tamil",
        "image_asset": "sugarcane_red_rot.jpg",
        "audio_asset": "sugarcane_redrot_ta_16k.wav",
        "voice_transcript_native": (
            "ஐயா, கரும்பு தண்டுக்குள் சிவப்பு நிறமாக மாறி நாற்றம் அடிக்கிறது. பயிர் முழுவதும் காய்கிறது. என்ன செய்வது?"
        ),
        "voice_transcript_english": (
            "Sir, inside the sugarcane stalk it has turned crimson red with a fermented smell. The whole crop is drying. What to do?"
        ),
        "disease_name": "Sugarcane Red Rot",
        "causative_pathogen": "Colletotrichum falcatum",
        "pathogen_type": "FUNGAL",
        "severity_percentage": 62.0,
        "disease_stage": "INTERNAL_VASCULAR_ROT",
        "visual_symptoms": [
            "Crimson-red pith discoloration with diagnostic white horizontal cross-bands",
            "Yellowing and drying of the third and fourth spindle leaves from top",
            "Alcoholic sour fermentation odor emanating from split canes",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.520,
            "ndvi_status": "CANOPY_VASCULAR_DECLINE",
            "ndwi": 0.310,
            "soil_moisture_m3m3": 0.40,
            "soil_status": "DELTA_ALLUVIAL_MOIST",
            "precipitation_next_4h_mm": 0.2,
            "precipitation_next_72h_mm": 4.0,
            "rain_probability_4h": 0.15,
        },
        "prescription": {
            "action_code": "SAFE_TO_SPRAY_IMMEDIATE",
            "banner_badge": "✅ CLEAR WINDOW: Immediate stool roguing and Trichoderma soil drenching required.",
            "wash_off_risk": "LOW",
            "hours_to_wait": 0,
            "recommended_window": "Today immediate root zone application",
            "treatment_mode": "SYSTEMIC_BIO_SANITATION_AND_DRENCHING",
            "treatment_name": "Trichoderma harzianum + Pseudomonas fluorescens Root Drench",
            "steps": [
                {
                    "step": 1,
                    "title": "Uproot Severely Affected Clumps",
                    "instruction": "Uproot completely dried sugarcane clumps and burn them outside the field to prevent mycelial spread.",
                },
                {
                    "step": 2,
                    "title": "Bio-Drench Furrows",
                    "instruction": "Drench adjacent healthy cane roots with Trichoderma harzianum (2.5 kg/ha mixed with well-rotted FYM).",
                },
                {
                    "step": 3,
                    "title": "Drain Stagnant Water",
                    "instruction": "Red rot spores travel through irrigation furrows; drain standing surface water immediately.",
                },
            ],
            "cost_inr": 95.0,
            "dealer_chemical_cost_inr": 850.0,
            "net_savings_inr": 755.0,
            "chemical_alternative": {
                "product": "Thiophanate Methyl 70% WP (1g/L) root drench",
                "withholding_period_days": 21,
            },
        },
        "audio_prescription_script": (
            "வணக்கம் திரு. முருகன். உங்கள் கரும்பில் செவ்வழுகல் நோய் (Red Rot) தீவிரமாக தாக்கியுள்ளது. பாதிக்கப்பட்ட கரும்புகளை உடனடியாக வேரோடு பிடுங்கி தீயிட்டு அழிக்கவும். வானிலை சாதகமாக உள்ளதால், உடனடியாக டிரைக்கோடெர்மா பூஞ்சாணக் கொல்லியை வேர்ப் பகுதியில் ஊற்றவும்."
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 3,
            "radius_km": 2.8,
            "message": "Alert: Red Rot confirmed in 3 adjacent sugarcane fields in Kumbakonam delta zone.",
        },
    },
    "dossier_f_wheat": {
        "id": "dossier_f_wheat",
        "title": "Dossier F: Haryana Wheat (Yellow Stripe Rust Air-Blast)",
        "farmer_name": "Balwant Singh",
        "village": "Taraori",
        "region": "Karnal District, Haryana",
        "country": "India",
        "coordinates": {"lat": 29.7280, "lng": 77.0250},
        "crop": "Wheat",
        "botanical_name": "Triticum aestivum",
        "language_code": "hi-IN",
        "language_name": "Hindi",
        "image_asset": "wheat_yellow_rust.jpg",
        "audio_asset": "wheat_rust_hi_16k.wav",
        "voice_transcript_native": (
            "बाबूजी, गेहूं की पत्तियों पर पीली-पीली हल्दी जैसी धारियां बन गई हैं। हाथ लगाने पर पीला पाउडर छूट रहा है।"
        ),
        "voice_transcript_english": (
            "Sir, bright yellow turmeric-like stripes have formed on wheat leaves. Yellow powder rubs off on hands. What spray is needed?"
        ),
        "disease_name": "Yellow / Stripe Rust",
        "causative_pathogen": "Puccinia striiformis f. sp. tritici",
        "pathogen_type": "FUNGAL",
        "severity_percentage": 51.0,
        "disease_stage": "RAPID_UREDINIAL_SPORULATION",
        "visual_symptoms": [
            "Narrow linear stripes of bright lemon-yellow uredinial pustules parallel to leaf veins",
            "Yellow powdery urediniospores easily rubbing off on fingers",
            "Premature drying and chlorosis of the flag leaf canopy",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.610,
            "ndvi_status": "EARLY_CANOPY_SENESCENCE",
            "ndwi": 0.180,
            "soil_moisture_m3m3": 0.26,
            "soil_status": "OPTIMAL_IRRIGATED_ALLUVIAL",
            "precipitation_next_4h_mm": 0.0,
            "precipitation_next_72h_mm": 0.0,
            "rain_probability_4h": 0.05,
        },
        "prescription": {
            "action_code": "SAFE_TO_SPRAY_IMMEDIATE",
            "banner_badge": "✅ CLEAR 72H WINDOW: Zero rain forecast. Spray bio-fungicide immediately to protect flag leaf.",
            "wash_off_risk": "LOW",
            "hours_to_wait": 0,
            "recommended_window": "Today midday (11:00 AM - 3:00 PM) after morning dew dries",
            "treatment_mode": "TARGETED_STRIPE_RUST_CONTAINMENT",
            "treatment_name": "Propiconazole 25% EC (Tilt) OR Pseudomonas fluorescens Foliar Wash",
            "steps": [
                {
                    "step": 1,
                    "title": "Wait for Dew Dissipation",
                    "instruction": "Ensure morning dew has evaporated completely from leaf blades before spraying to prevent active dilution.",
                },
                {
                    "step": 2,
                    "title": "Flag Leaf Canopy Spray",
                    "instruction": "Spray Propiconazole 25% EC at 1ml per liter water (200ml in 200L water per acre) ensuring flag leaf coverage.",
                },
                {
                    "step": 3,
                    "title": "Monitor Downwind Fields",
                    "instruction": "Airborne spores travel on westerly winds; notify neighbors within 5km radius.",
                },
            ],
            "cost_inr": 110.0,
            "dealer_chemical_cost_inr": 780.0,
            "net_savings_inr": 670.0,
            "chemical_alternative": {
                "product": "Propiconazole 25% EC (1ml/L) OR Tebuconazole 25.9% EC (1ml/L)",
                "withholding_period_days": 28,
            },
        },
        "audio_prescription_script": (
            "राम-राम बलवंत जी। आपके गेहूं में पीला रतुआ यानी स्ट्राइप रस्ट आ चुका है। मौसम बिल्कुल साफ है और अगले तीन दिनों तक बारिश नहीं होगी। आज ही दोपहर में ओस सूखने के बाद प्रोपिकोनाज़ोल का छिड़काव तुरंत करें ताकि झंडा पत्ता बचाया जा सके।"
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 8,
            "radius_km": 4.6,
            "message": "Critical Alert: Yellow Rust spores moving rapidly across 8 wheat plots in Karnal district.",
        },
    },
    "dossier_g_soybean": {
        "id": "dossier_g_soybean",
        "title": "Dossier G: Vietnam Central Highlands Soybean (Asian Rust Wash-Off)",
        "farmer_name": "Nguyen Van Hai",
        "village": "Cu M'gar",
        "region": "Dak Lak Province",
        "country": "Vietnam",
        "coordinates": {"lat": 12.8680, "lng": 108.1250},
        "crop": "Soybean (Đậu nành)",
        "botanical_name": "Glycine max",
        "language_code": "vi-VN",
        "language_name": "Vietnamese",
        "image_asset": "soybean_asian_rust.jpg",
        "audio_asset": "soybean_rust_vi_16k.wav",
        "voice_transcript_native": (
            "Thưa chuyên gia, mặt dưới lá đậu nành có nhiều đốm nhỏ li ti màu nâu đỏ như rỉ sắt, lá đang rụng nhiều. Tôi nên phun thuốc gì?"
        ),
        "voice_transcript_english": (
            "Expert, the underside of soybean leaves has countless tiny reddish-brown spots like iron rust, and leaves are dropping heavily. What should I spray?"
        ),
        "disease_name": "Asian Soybean Rust",
        "causative_pathogen": "Phakopsora pachyrhizi",
        "pathogen_type": "FUNGAL",
        "severity_percentage": 46.5,
        "disease_stage": "ACTIVE_FOLIAR_PUSTULE_ERUPTION",
        "visual_symptoms": [
            "Dense polygonal tan to dark reddish-brown lesions on abaxial (underside) leaf surface",
            "Raised volcano-shaped uredinial pustules erupting through epidermis",
            "Rapid premature defoliation starting from lower canopy moving upward",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.440,
            "ndvi_status": "SEVERE_CANOPY_DEFOLIATION",
            "ndwi": 0.220,
            "soil_moisture_m3m3": 0.32,
            "soil_status": "BASALTIC_RED_SOIL_WET",
            "precipitation_next_4h_mm": 22.0,
            "precipitation_next_72h_mm": 68.0,
            "rain_probability_4h": 0.92,
        },
        "prescription": {
            "action_code": "HALT_SPRAYING_RAIN_IMMINENT",
            "banner_badge": "⛔ HALT: Heavy monsoon downpour (22mm) arriving in 2 hours. Do not spray.",
            "wash_off_risk": "CRITICAL",
            "hours_to_wait": 20,
            "recommended_window": "Tomorrow morning after convective squall passes",
            "treatment_mode": "ORGANIC_COPPER_AND_BACILLUS_BARRIER",
            "treatment_name": "Bacillus subtilis + Copper Hydroxide Foliar Barrier",
            "steps": [
                {
                    "step": 1,
                    "title": "Hold Spraying Operation",
                    "instruction": "Tropical convective storm with 22mm rainfall arriving within 2 hours will wash away 100% of sprayed chemicals.",
                },
                {
                    "step": 2,
                    "title": "Prepare Underside Spray Equipment",
                    "instruction": "Calibrate nozzle angle upward to ensure under-leaf coverage where Phakopsora uredinia reside.",
                },
                {
                    "step": 3,
                    "title": "Apply After Weather Window Clears",
                    "instruction": "Spray tomorrow morning during the 18-hour clear window.",
                },
            ],
            "cost_inr": 75.0,
            "dealer_chemical_cost_inr": 620.0,
            "net_savings_inr": 545.0,
            "chemical_alternative": {
                "product": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (1ml/L)",
                "withholding_period_days": 21,
            },
        },
        "audio_prescription_script": (
            "Chào bác Hải. Cây đậu nành của bác bị bệnh rỉ sắt Châu Á rất nặng. Cảnh báo khẩn cấp: rada thời tiết dự báo 2 giờ nữa sẽ có mưa to 22mm, tuyệt đối không được phun thuốc hôm nay vì thuốc sẽ bị rửa trôi hoàn toàn. Bác hãy đợi sáng mai trời ráo rồi phun thuốc vào mặt dưới lá."
        ),
        "outbreak_alert": {
            "is_cluster": True,
            "nearby_farms_count": 5,
            "radius_km": 3.5,
            "message": "High Alert: Asian Soybean Rust spreading across 5 farms in Cu M'gar district.",
        },
    },
    "dossier_edge_sunscorch": {
        "id": "dossier_edge_sunscorch",
        "title": "Negative Control 1: Physiological Sun-Scorch Bleaching",
        "farmer_name": "Anand Patil",
        "village": "Sangli District",
        "region": "Western Maharashtra",
        "country": "India",
        "coordinates": {"lat": 16.8920, "lng": 74.6850},
        "crop": "Soybean / Pulses",
        "botanical_name": "Glycine max",
        "language_code": "mr-IN",
        "language_name": "Marathi",
        "image_asset": "sunscorch_control.jpg",
        "audio_asset": "cotton_blight_mr_16k.wav",
        "voice_transcript_native": (
            "पानांवर पांढरे चट्टे पडले आहेत. हे कोणतं बुरशीजन्य रोग आहे का? दुकानदाराने औषध घ्यायला सांगितलं आहे."
        ),
        "voice_transcript_english": (
            "White bleached patches have appeared on the leaves. Is this a fungal disease? The dealer advised me to buy fungicide."
        ),
        "disease_name": "Physiological Sun-Scorch (Abiotic Sunburn)",
        "causative_pathogen": "None (Abiotic Intense Solar Radiation)",
        "pathogen_type": "ABIOTIC_PHYSIOLOGICAL",
        "severity_percentage": 15.0,
        "disease_stage": "NON_PATHOGENIC_TISSUE_BLEACHING",
        "visual_symptoms": [
            "Bleached papery white-tan dry patches strictly confined to upper sun-exposed leaves",
            "Absence of chlorotic yellow halos or water-soaked borders",
            "Total absence of fungal pycnidia, mycelia, or bacterial ooze",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.680,
            "ndvi_status": "VIGOROUS_HEALTHY_CANOPY",
            "ndwi": 0.080,
            "soil_moisture_m3m3": 0.22,
            "soil_status": "MODERATE_MOISTURE",
            "precipitation_next_4h_mm": 0.0,
            "precipitation_next_72h_mm": 0.0,
            "rain_probability_4h": 0.01,
        },
        "prescription": {
            "action_code": "NO_PATHOLOGY_PHYSIOLOGICAL_SUNSCORCH",
            "banner_badge": "🛑 ZERO CHEMICALS: This is sun-scorch (sunburn), not a disease. Do not buy fungicide.",
            "wash_off_risk": "N/A",
            "hours_to_wait": 0,
            "recommended_window": "Maintain regular soil irrigation",
            "treatment_mode": "ABIOTIC_MANAGEMENT_NO_CHEMICALS",
            "treatment_name": "Canopy Hydration & Light Irrigation (No Chemical Pesticides)",
            "steps": [
                {
                    "step": 1,
                    "title": "Reject Chemical Purchases",
                    "instruction": "This is non-pathogenic sunburn bleaching from sudden cloud clearing. Chemical fungicides are 100% ineffective and waste ₹700.",
                },
                {
                    "step": 2,
                    "title": "Irrigate to Relieve Heat Stress",
                    "instruction": "Provide a light evening irrigation to replenish canopy turgor pressure.",
                },
            ],
            "cost_inr": 0.0,
            "dealer_chemical_cost_inr": 700.0,
            "net_savings_inr": 700.0,
            "chemical_alternative": {
                "product": "No chemicals recommended. Abiotic physiological condition.",
                "withholding_period_days": 0,
            },
        },
        "audio_prescription_script": (
            "आनंदजी, तुमच्या पिकावर कोणताही रोग किंवा बुरशी लागलेली नाही. हे कडक उन्हामुळे पानांना बसलेले चटके (सन-स्कॉर्च) आहेत. कृषी सेवा केंद्रातून कोणतेही रासायनिक बुरशीनाशक खरेदी करू नका, तुमचे ७०० रुपये वाचतील. फक्त संध्याकाळी हलके पाणी द्या."
        ),
        "outbreak_alert": {
            "is_cluster": False,
            "nearby_farms_count": 0,
            "radius_km": 0.0,
            "message": "Abiotic physiological condition. No epidemiological outbreak risk.",
        },
    },
    "dossier_edge_mechanical": {
        "id": "dossier_edge_mechanical",
        "title": "Negative Control 2: Mechanical Hail & Machinery Tear",
        "farmer_name": "Harpreet Dhillon",
        "village": "Ludhiana District",
        "region": "Central Plain, Punjab",
        "country": "India",
        "coordinates": {"lat": 30.8250, "lng": 75.7650},
        "crop": "Maize / Fodder",
        "botanical_name": "Zea mays",
        "language_code": "hi-IN",
        "language_name": "Hindi",
        "image_asset": "mechanical_injury.jpg",
        "audio_asset": "wheat_rust_hi_16k.wav",
        "voice_transcript_native": (
            "खेत में पत्तियों के चीरे लग गए हैं और फट गई हैं। क्या कोई कीड़ा या बीमारी है? क्या दवाई छिड़कें?"
        ),
        "voice_transcript_english": (
            "Leaf blades in the field are slit and ripped. Is this an insect pest or bacterial disease? What medicine should we spray?"
        ),
        "disease_name": "Mechanical Hail Damage & Equipment Tear",
        "causative_pathogen": "None (Abiotic Physical Trauma)",
        "pathogen_type": "ABIOTIC_MECHANICAL",
        "severity_percentage": 20.0,
        "disease_stage": "PHYSICAL_LACERATION",
        "visual_symptoms": [
            "Irregular physical tears and ragged longitudinal leaf fractures along veins",
            "Bruised midrib injuries consistent with hail impact and machinery brush",
            "Clean wound margins without water-soaking, bacterial ooze, or fungal halos",
        ],
        "satellite_telemetry": {
            "source": "COPERNICUS/S2_SR (Sentinel-2)",
            "ndvi": 0.580,
            "ndvi_status": "SLIGHT_MECHANICAL_DEFOLIATION",
            "ndwi": 0.150,
            "soil_moisture_m3m3": 0.25,
            "soil_status": "MOIST_LOAM",
            "precipitation_next_4h_mm": 0.0,
            "precipitation_next_72h_mm": 0.0,
            "rain_probability_4h": 0.04,
        },
        "prescription": {
            "action_code": "MECHANICAL_INJURY_MAINTAIN_NUTRITION",
            "banner_badge": "🛑 DO NOT SPRAY PESTICIDES: Physical laceration from hailstorm/machinery, not an infection.",
            "wash_off_risk": "N/A",
            "hours_to_wait": 0,
            "recommended_window": "Foliar micronutrient spray in 3-4 days after wound callusing",
            "treatment_mode": "WOUND_HEALING_NUTRITION",
            "treatment_name": "Foliar 1% Urea / Micronutrient Spray (Post-Callus Healing)",
            "steps": [
                {
                    "step": 1,
                    "title": "Avoid Pesticide Dumping",
                    "instruction": "This is mechanical physical tearing from recent hail and machinery pass. Pesticides will only cause chemical leaf burn.",
                },
                {
                    "step": 2,
                    "title": "Support Natural Callusing",
                    "instruction": "Allow wound margins to dry and callus naturally for 3 days before any light foliar nutrition.",
                },
            ],
            "cost_inr": 30.0,
            "dealer_chemical_cost_inr": 800.0,
            "net_savings_inr": 770.0,
            "chemical_alternative": {
                "product": "No chemical pesticide required. Optional: Copper Oxychloride (1.5g/L) strictly if secondary bacterial ooze appears.",
                "withholding_period_days": 0,
            },
        },
        "audio_prescription_script": (
            "हरप्रीत जी, आपकी फसल में कोई कीड़ा या बीमारी नहीं है। यह हालिया ओलावृष्टि और ट्रैक्टर मशीनरी से पत्तों का कटना-फटना है। किसी भी कीटनाशक या फफूंदनाशक का छिड़काव न करें, इससे सिर्फ नुकसान होगा और आपके ८०० रुपये बचेंगे।"
        ),
        "outbreak_alert": {
            "is_cluster": False,
            "nearby_farms_count": 0,
            "radius_km": 0.0,
            "message": "Physical mechanical injury. Zero epidemiological spread risk.",
        },
    },
}
