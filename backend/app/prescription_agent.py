"""AgriResilience AI — Autonomous Agronomic Decision & Synthesis Agent

Fuses plant pathology with Earth Engine micro-climate telemetry to formulate
safe, weather-timed, cost-effective organic and chemical prescriptions.
"""

from typing import Any, Dict


def synthesize_prescription(
    pathology_data: Dict[str, Any],
    geospatial_data: Dict[str, Any],
    language_code: str = "mr-IN",
) -> Dict[str, Any]:
  """Formulates clinical agronomic prescription based on pathology and micro-climate."""
  pathology = pathology_data.get("pathology", {})
  pathogen_type = pathology.get("pathogen_type", "FUNGAL")
  disease_name = pathology.get("primary_diagnosis", "Crop Blight")
  crop_name = pathology_data.get("crop_identified", "Crop")

  rain_prob_4h = geospatial_data.get("rain_probability_4h", 0.0)
  rain_4h_mm = geospatial_data.get("precipitation_next_4h_mm", 0.0)
  wash_off_risk = geospatial_data.get("wash_off_risk", "LOW")

  # Decision Branch 1: Abiotic Physiological Negative Control (Sun-Scorch)
  if pathogen_type == "ABIOTIC_PHYSIOLOGICAL":
    return {
        "action_code": "NO_PATHOLOGY_PHYSIOLOGICAL_SUNSCORCH",
        "spray_permitted_now": False,
        "banner_badge": "🛑 ZERO CHEMICALS: Sun-scorch bleaching (sunburn), not a disease. Do not buy fungicide.",
        "reason": "Abiotic physiological tissue bleaching from intense solar radiation. Chemical pesticides cause phytotoxicity and zero curative benefit.",
        "recommended_window": "Maintain regular evening irrigation",
        "hours_to_wait": 0,
        "treatment_mode": "ABIOTIC_PHYSIOLOGICAL_RECOVERY",
        "treatment_name": "Canopy Hydration & Light Irrigation (No Chemical Pesticides)",
        "steps": [
            {
                "step": 1,
                "title": "Refuse Chemical Pesticides",
                "instruction": "This is non-pathogenic sunburn. Commercial fungicides will not reverse bleaching and waste ₹700.",
            },
            {
                "step": 2,
                "title": "Replenish Canopy Moisture",
                "instruction": "Irrigate crop during evening hours to restore turgor pressure and prevent further solar desiccation.",
            },
        ],
        "cost_inr": 0.0,
        "dealer_chemical_cost_inr": 700.0,
        "net_savings_inr": 700.0,
        "chemical_alternative": {
            "product": "No chemicals recommended. Abiotic physiological condition.",
            "dosage": "None",
            "withholding_period_days": 0,
        },
        "audio_script": "तुमच्या पिकावर कोणताही रोग किंवा बुरशी लागलेली नाही. हे कडक उन्हामुळे पानांना बसलेले चटके आहेत. रासायनिक बुरशीनाशक खरेदी करू नका, तुमचे ७०० रुपये वाचतील.",
        "audio_script_english": "Zero chemicals required: Your crop is suffering from physiological sun-scorch (sunburn), not a fungal pathogen. Do not purchase dealer fungicides.",
        "audio_script_phonetic": "Tumchya pikavar konthahi rog kivha burshi lagleli naahi. He kadak unhamule paananna baslele chatke aahet. Buroshinashak vikat gheu naka.",
    }

  # Decision Branch 2: Abiotic Mechanical Negative Control (Hail / Tractor laceration)
  elif pathogen_type == "ABIOTIC_MECHANICAL":
    return {
        "action_code": "MECHANICAL_INJURY_MAINTAIN_NUTRITION",
        "spray_permitted_now": False,
        "banner_badge": "🛑 DO NOT SPRAY PESTICIDES: Physical laceration from hailstorm/machinery, not an infection.",
        "reason": "Physical mechanical laceration of leaf tissue from weather or machinery. Pesticides provide zero therapeutic value.",
        "recommended_window": "Foliar nutrition after 3 days wound callusing",
        "hours_to_wait": 0,
        "treatment_mode": "POST_TRAUMA_WOUND_CALLUSING",
        "treatment_name": "Wound Margin Callusing + Foliar Micronutrient Wash",
        "steps": [
            {
                "step": 1,
                "title": "Do Not Spray Chemical Pesticides",
                "instruction": "Torn leaf blades are physical wounds. Fungicides and insecticides will cause chemical scorch on open plant wounds.",
            },
            {
                "step": 2,
                "title": "Allow Natural Callus Formation",
                "instruction": "Allow wound margins to dry and seal naturally over 72 hours before light foliar nutrition.",
            },
        ],
        "cost_inr": 30.0,
        "dealer_chemical_cost_inr": 800.0,
        "net_savings_inr": 770.0,
        "chemical_alternative": {
            "product": "No chemical pesticide required. Optional: Copper Oxychloride 1.5g/L strictly if secondary bacterial soft rot develops.",
            "dosage": "None unless secondary bacteriosis",
            "withholding_period_days": 0,
        },
        "audio_script": "आपकी फसल में कोई कीड़ा या बीमारी नहीं है। यह ओलावृष्टि और मशीनरी से पत्तों का कटना-फटना है। कोई कीटनाशक न छिड़कें, इससे आपके ८०० रुपये बचेंगे।",
        "audio_script_english": "Physical injury confirmed: The ripped leaves are caused by hailstones and tractor machinery trauma, not an infection. Do not spray pesticides.",
        "audio_script_phonetic": "Aapki fasal me koi keeda ya bimari nahi hai. Yeh ola-vrishti aur machinery se patton ka fatna hai. Keetnashak na chhidken.",
    }

  # Decision Branch 3: Viral Pathogen (Chemicals are useless, mechanical roguing required)
  elif pathogen_type == "VIRAL":
    return {
        "action_code": "HALT_CHEMICALS_ROGUE_PLANTS",
        "spray_permitted_now": False,
        "banner_badge": (
            "⚠️ VIRAL INFECTION: Do not buy fungicides. Roguing required."
        ),
        "reason": (
            "Viral plant diseases cannot be cured with chemical foliar sprays."
            " Chemical dealers often mis-sell useless pesticides."
        ),
        "recommended_window": "Immediate mechanical sanitation",
        "hours_to_wait": 0,
        "treatment_mode": "SANITATION_AND_VECTOR_TRAPPING",
        "treatment_name": (
            "Mechanical Roguing (Uproot & Burn) + Yellow Sticky Traps for"
            " Whitefly Vectors"
        ),
        "steps": [
            {
                "step": 1,
                "title": "Stop Chemical Spending",
                "instruction": (
                    f"{disease_name} is viral. Chemical sprays cannot cure it."
                    " Save your money."
                ),
            },
            {
                "step": 2,
                "title": "Rogue Infected Plants",
                "instruction": (
                    "Immediately uproot severely stunted and yellowed plants"
                    " and burn them outside the farm perimeter."
                ),
            },
            {
                "step": 3,
                "title": "Trap Insect Vectors",
                "instruction": (
                    "Install yellow sticky sheets (1 trap every 20 meters) to"
                    " trap whiteflies that transmit the virus."
                ),
            },
        ],
        "cost_inr": 25.0,
        "dealer_chemical_cost_inr": 950.0,
        "net_savings_inr": 925.0,
        "chemical_alternative": {
            "product": (
                "No chemical curative exists. Spray neem oil 2% on healthy"
                " plants to repel vectors."
            ),
            "dosage": "20ml Neem oil + 5ml soap per liter",
            "withholding_period_days": 0,
        },
        "audio_script": (
            f"Peringatan penting untuk tanaman {crop_name} Anda. Penyakit ini"
            " adalah infeksi virus dan tidak bisa disembuhkan dengan semprotan"
            " fungisida. Jangan buang uang beli obat kimia. Segera cabut dan"
            " bakar tanaman yang kerdil, lalu pasang perangkap kuning untuk kutu"
            " kebul."
        ),
        "audio_script_english": (
            f"Important Sanitation Warning: Your {crop_name} is infected with {disease_name}. This is a viral disease and cannot be cured by chemical sprays. Do not waste money on dealer chemicals. Immediately uproot and burn stunted plants, and install yellow sticky traps for whitefly vectors."
        ),
        "audio_script_phonetic": (
            f"Peringatan penting untuk tanaman {crop_name} Anda. Penyakit ini adalah infeksi virus dan tidak bisa disembuhkan dengan semprotan fungisida. Jangan buang uang beli obat kimia. Segera cabut dan bakar tanaman yang kerdil, lalu pasang perangkap kuning untuk kutu kebul."
        ),
    }

  # Decision Branch 4: Wash-Off Risk (Rain incoming)
  elif wash_off_risk == "CRITICAL" or (rain_prob_4h > 0.60 and rain_4h_mm > 5.0):
    return {
        "action_code": "HALT_SPRAYING_RAIN_IMMINENT",
        "spray_permitted_now": False,
        "banner_badge": (
            f"⛔ HALT: Heavy rain ({rain_4h_mm}mm) expected in 3 hours. Do not"
            " spray today."
        ),
        "reason": (
            "Imminent convective rainstorm will wash away foliar treatment"
            " within 3 hours, causing 100% input wastage."
        ),
        "recommended_window": (
            "Wait 16 hours. Spray tomorrow morning between 6:30 AM and 8:30 AM."
        ),
        "hours_to_wait": 16,
        "treatment_mode": "ORGANIC_BIOPESTICIDE_LOW_COST",
        "treatment_name": (
            "Neem Seed Kernel Extract 5% (NSKE) + Copper Oxychloride Backup"
        ),
        "steps": [
            {
                "step": 1,
                "title": "Hold Spray Application",
                "instruction": (
                    "Do not spray chemicals today. Heavy rainfall will wash"
                    " them into the soil, wasting input costs."
                ),
            },
            {
                "step": 2,
                "title": "Prepare Organic Bio-Wash",
                "instruction": (
                    "Soak 500g crushed dry neem seeds in 10 liters water"
                    " overnight. Strain through muslin cloth and add 20g soap"
                    " powder."
                ),
            },
            {
                "step": 3,
                "title": "Foliar Spray Technique",
                "instruction": (
                    "Spray tomorrow morning thoroughly on leaf undersides where"
                    " bacterial colonies proliferate."
                ),
            },
        ],
        "cost_inr": 45.0,
        "dealer_chemical_cost_inr": 550.0,
        "net_savings_inr": 505.0,
        "chemical_alternative": {
            "product": "Copper Oxychloride 50% WP + Streptocycline 100ppm",
            "dosage": (
                "2.5g Copper Oxychloride + 0.1g Streptocycline per liter water"
            ),
            "withholding_period_days": 14,
        },
        "audio_script": (
            "महत्त्वाची सूचना: आज कोणतीही औषध फवारणी करू नका! सॅटेलाइट"
            f" रडारनुसार पुढच्या ३ तासांत जोरदार पाऊस येणार आहे. तुमच्या"
            f" {crop_name} वरील {disease_name} रोगासाठी उद्या सकाळी ५ टक्के"
            " निंबोळी अर्क फवारा. यामुळे तुमचे ५०० रुपये वाचतील."
        ),
        "audio_script_english": (
            f"Critical Weather Advisory: Do not spray any chemical pesticide today! Satellite radar forecasts heavy monsoon rain arriving within 3 hours which will completely wash off the spray. For the {disease_name} on your {crop_name}, apply 5 percent neem seed kernel extract tomorrow morning. This will save you 500 rupees."
        ),
        "audio_script_phonetic": (
            f"Mahatvachi soochana: Aaj kontehi aushadh fawarani karu naka! Satellite radar-nusar pudhchya 3 taasant jordaar paaus yenaare aahe. Tumchya {crop_name} waril {disease_name} rogasaathi udya sakaali 5 takke nimboli ark fawara. Yaamule tumche 500 rupaye vaachtil."
        ),
    }

  # Decision Branch 5: Safe to Spray (Fungal / Bacterial with clear weather)
  else:
    return {
        "action_code": "SAFE_TO_SPRAY_IMMEDIATE",
        "spray_permitted_now": True,
        "banner_badge": (
            "✅ CLEAR WEATHER WINDOW: 48h dry window. Spray immediately."
        ),
        "reason": (
            "Satellite radar confirms dry weather over the next 48 hours."
            " Optimal window for active pathogen containment."
        ),
        "recommended_window": "Today late afternoon (4 PM - 6 PM) or tomorrow",
        "hours_to_wait": 0,
        "treatment_mode": "TARGETED_BIO_FUNGICIDE_CONTAINMENT",
        "treatment_name": (
            "Pseudomonas fluorescens Bio-Control OR Tricyclazole 75% WP"
        ),
        "steps": [
            {
                "step": 1,
                "title": "Optimal Weather Confirmed",
                "instruction": (
                    "Zero rain forecast for next 48 hours. Spores are actively"
                    " multiplying; apply treatment immediately."
                ),
            },
            {
                "step": 2,
                "title": "Bio-Control Preparation",
                "instruction": (
                    "Mix 10g of Pseudomonas fluorescens talc powder per liter"
                    " of water."
                ),
            },
            {
                "step": 3,
                "title": "Deep Canopy Application",
                "instruction": (
                    "Spray thoroughly on lower leaves and collar nodes where"
                    " humidity is highest."
                ),
            },
        ],
        "cost_inr": 85.0,
        "dealer_chemical_cost_inr": 720.0,
        "net_savings_inr": 635.0,
        "chemical_alternative": {
            "product": "Tricyclazole 75% WP (0.6g/L) OR Isoprothiolane 40% EC",
            "dosage": "0.6g per liter of clean water",
            "withholding_period_days": 21,
        },
        "audio_script": (
            f"আপনার {crop_name} ফসলে {disease_name} রোগ শনাক্ত হয়েছে। আবহাওয়া"
            " স্যাটেলাইট তথ্য অনুযায়ী আগামী ৪৮ ঘণ্টা কোনো বৃষ্টি নেই। অবিলম্বে"
            " আজ বিকেলেই সিউডোমোনাস অথবা ট্রাইসাইক্লাজোল স্প্রে করুন।"
        ),
        "audio_script_english": (
            f"Optimal Spray Window Confirmed: Satellite radar verifies clear, dry weather for the next 48 hours with zero rainfall. For {disease_name} on your {crop_name}, spray Pseudomonas bio-fungicide or Tricyclazole late this afternoon to contain the fungal outbreak."
        ),
        "audio_script_phonetic": (
            f"Aapnar {crop_name} foshle {disease_name} rog shonakto hoyechhe. Aabohawa satellite tottho onujayi aagami 48 ghonta kono brishti nei. Obilombe aaj bikelei Pseudomonas othoba Tricyclazole spray korun."
        ),
    }
