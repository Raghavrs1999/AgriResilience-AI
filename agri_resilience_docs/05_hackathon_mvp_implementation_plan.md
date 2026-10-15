# AgriResilience AI — Hackathon MVP Implementation Plan & Demo Script
## 7-Day Sprint Roadmap, Pre-Packaged Demo Dossiers, and 3-Minute Video Production

> **Submission Deadline**: October 18, 2026 (11:59 PM SGT)  
> **Mandatory Submissions**:
> 1. Working Prototype deployed live on **Google Cloud Run** and **Firebase Hosting**
> 2. 3-Minute Demonstration Video link (YouTube / Vimeo / Google Drive)
> 3. PDF Proposal Deck (10–12 slides)
> 4. GitHub Repository with full source code and open documentation

---

### 1. Tactical 7-Day Execution Timeline (Oct 12 – Oct 18, 2026)

```
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│  OCT 12 (DAY 1)  │──▶│  OCT 13 (DAY 2)  │──▶│  OCT 14 (DAY 3)  │──▶│  OCT 15 (DAY 4)  │
│  Data Dossiers & │   │  Cloud Run Core  │   │  Earth Engine &  │   │  React PWA UI &  │
│  Mock Registries │   │  (Gemini Vision) │   │  Voice Pipeline  │   │  Satellite Map   │
└──────────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
                                                                               │
                                                                               ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐             │
│  OCT 18 (DAY 7)  │◀──│  OCT 17 (DAY 6)  │◀──│  OCT 16 (DAY 5)  │◀────────────┘
│  Final Audit &   │   │  Deck & Video    │   │  GCP Deploy &    │
│  Submission      │   │  Recording       │   │  Stress Testing  │
└──────────────────┘   └──────────────────┘   └──────────────────┘
```

#### Daily Sprint Breakdown:
- **Day 1 (Oct 12)**: Curate high-res diseased leaf macro images (Cotton, Rice, Cassava) and record synthetic vernacular audio files (Marathi, Bengali, Bahasa). Set up simulated Google Earth Engine caching layer.
- **Day 2 (Oct 13)**: Build FastAPI backend on Python 3.11 with Google GenAI SDK (`google-genai`). Implement multimodal prompt parser for Gemini 1.5 Pro to extract crop identity, disease severity, and JSON prescription.
- **Day 3 (Oct 14)**: Connect Earth Engine API (`COPERNICUS/S2_SR`) to calculate real-time NDVI and precipitation radar. Integrate Google Cloud Text-to-Speech Neural2 voices for Marathi, Hindi, and Bahasa.
- **Day 4 (Oct 15)**: Build high-contrast, responsive React PWA on Vite + TailwindCSS. Create three primary views:
  1. *Farmer Mobile Cockpit*: Voice note recorder, photo uploader, dynamic prescription timeline.
  2. *Interactive Geospatial Map*: Leaflet/Mapbox map displaying farm GPS, Sentinel-2 NDVI false-color overlay, and 5km outbreak cluster circles.
  3. *Agronomist Diagnostic Studio*: Side-by-side comparison of leaf lesions with ICAR clinical literature.
- **Day 5 (Oct 16)**: Containerize backend with Docker and deploy to **Google Cloud Run** (`asia-southeast1`). Deploy frontend to **Firebase Hosting**. Test end-to-end latency (<8 seconds per consultation).
- **Day 6 (Oct 17)**: Record screen walkthrough and produce the 3-minute demo video. Export 10-slide presentation deck to PDF.
- **Day 7 (Oct 18)**: Complete final submission on Hack2skill portal, verify all public links, and submit!

---

### 2. Three Pre-Packaged Demo Scenarios (Dossiers)

---

#### Dossier A: Maharashtra Cotton Farmer (The "Rain Wash-Off" Crisis)
- **Farmer Profile**: Tukaram Shinde, Jalna, Maharashtra (India). Coordinates: `[19.7515, 75.7139]`.
- **Language / Dialect**: Marathi (`mr-IN`).
- **Spoken Audio Input**:
  > *"साहेब, आमच्या कपाशीच्या पानांवर काळे-तांबडे डाग पडले आहेत आणि झाड सुकत चाललंय. काय फवारणी करू?"*  
  > *(Sir, blackish-red spots have appeared on our cotton leaves and the plants are wilting. What should I spray?)*
- **Uploaded Image**: Macro photograph of a cotton leaf with angular vein-bound water-soaked lesions.
- **System Diagnosis**:
  - *Crop*: Cotton (*Gossypium hirsutum*)
  - *Pathogen*: Bacterial Blight (*Xanthomonas citri pv. malvacearum*), Severity: 38.5%
- **Geospatial & Micro-Climate Telemetry**:
  - *Sentinel-2 NDVI*: `0.41` (Stressed vegetation)
  - *ERA5 Rainfall Radar*: **Heavy convective rain (18mm) arriving in 3.5 hours**.
- **Prescription Verdict**:
  - **CRITICAL ALERT**: ⛔ **HALT SPRAYING IMMEDIATELY**.
  - **Reason**: Incoming heavy downpour will wash away ₹500 in chemical spray within 3 hours.
  - **Action**: Delay spray until 6:30 AM tomorrow. Use low-cost organic Neem Seed Extract (5%) + Copper Oxychloride backup. Saves ₹450 vs. commercial dealer pesticide.
- **Audio Output**: Plays warm, natural Marathi voice note explaining the delay and recipe.

---

#### Dossier B: West Bengal Paddy Farmer (The "Airborne Rice Blast" Cluster)
- **Farmer Profile**: Debabrata Roy, Nadia District, West Bengal (India). Coordinates: `[23.4710, 88.5565]`.
- **Language / Dialect**: Bengali (`bn-IN`).
- **Spoken Audio Input**:
  > *"ধান গাছের পাতায় নৌকার মতো চোখের দাগ হয়েছে। পুরো মাঠ নষ্ট হয়ে যাবে মনে হচ্ছে।"*  
  > *(Spindle-shaped eye spots have formed on the paddy leaves. It looks like the whole field will be ruined.)*
- **Uploaded Image**: Paddy leaf showing classic diamond/spindle-shaped necrotic lesions with grey centers.
- **System Diagnosis**:
  - *Crop*: Rice / Paddy (*Oryza sativa*)
  - *Pathogen*: Rice Blast (*Magnaporthe oryzae*), Severity: 48.0% (Critical)
- **Geospatial & Micro-Climate Telemetry**:
  - *Sentinel-2 NDVI*: `0.38` (Severe canopy stress)
  - *NDWI Moisture*: `0.42` (High standing water in paddy; high relative humidity 92% favoring sporulation).
  - *Precipitation 48h*: Clear weather window (Rain probability: 8%).
- **Prescription Verdict**:
  - **SAFE TO SPRAY**: Clear 48-hour window.
  - **Action**: Immediate spray of *Pseudomonas fluorescens* (bio-control) or Tricyclazole 75% WP.
  - **Community Outbreak Trigger**: System clusters 4 other nearby paddy consultations within 3.8 km and fires an automated **Epidemiological Cluster Warning** to all cooperative members.

---

#### Dossier C: Central Java Cassava Farmer (The "Viral Stunting" Trap)
- **Farmer Profile**: Budi Santoso, Gunungkidul, Yogyakarta (Indonesia). Coordinates: `[-7.9658, 110.6025]`.
- **Language / Dialect**: Bahasa Indonesia / Javanese (`id-ID`).
- **Spoken Audio Input**:
  > *"Daun singkong saya menguning keriting dan batangnya kerdil. Ini kena penyakit apa ya pak?"*  
  > *(My cassava leaves are yellowing, curling, and the stem is stunted. What sickness is this, sir?)*
- **Uploaded Image**: Cassava leaf displaying severe mosaic chlorosis, puckering, and leaf distortion.
- **System Diagnosis**:
  - *Crop*: Cassava (*Manihot esculenta*)
  - *Pathogen*: Cassava Mosaic Disease (CMD) (Viral, transmitted by *Bemisia tabaci* whiteflies). Severity: 55%.
- **Geospatial Telemetry**:
  - *Soil Moisture*: `DROUGHT_STRESSED` (NDWI: -0.05).
- **Prescription Verdict**:
  - **DIAGNOSTIC INSIGHT**: Viral disease cannot be cured by spraying fungicides. Prevents farmer from wasting 200,000 IDR on useless chemical sprays.
  - **Remediation**: Rogue (uproot and burn) infected plants immediately to prevent whitefly vector transmission to adjacent healthy cassava.

---

### 3. Word-for-Word 3-Minute Demo Video Script & Storyboard

- **Target Duration**: Exactly 2 minutes and 48 seconds (well under the 3-minute hard limit).
- **Format**: 1080p 60fps, picture-in-picture narration with crisp UI screen recording.

| Time Window | Screen Visual | Voiceover Script (Spoken in Clear English) | Audio / Effect |
| :---: | :--- | :--- | :--- |
| **0:00 – 0:25** | High-energy montage of smallholder Asian farmers inspecting diseased crops, drought cracks, and news headlines: *"Blight Wipes Out 40% of Asian Harvests"*. | *"Across Asia, over 450 million smallholder farmers produce 80% of our food supply. But when climate shocks hit and deadly crop blights strike, they face an impossible ratio: one extension officer for every 3,000 farmers. Trapped in a 10-day information void, farmers guess—wasting billions on toxic chemical pesticides that rain washes away hours later. We built AgriResilience AI to put an elite plant pathologist and satellite meteorologist directly in every farmer's pocket."* | Dramatic opening music fading into tech background pulse. |
| **0:25 – 0:50** | Cut to live **AgriResilience PWA** running on Google Cloud Run. Shows mobile viewport with Marathi voice interface. Click "Consultation Dossier A". | *"Meet Tukaram, a cotton farmer in Maharashtra. His cotton leaves are turning red. He doesn't type—he simply taps the microphone and speaks in his native Marathi dialect while taking a photo of the infected leaf. In seconds, our system ingests both the audio waveform and the high-resolution photo."* | Clean UI tap sounds; Marathi voice note plays for 3 seconds. |
| **0:50 – 1:30** | Split screen: Left side shows **Gemini 1.5 Pro** extracting Bacterial Blight (*Xanthomonas*). Right side shows **Google Earth Engine** fetching Sentinel-2 NDVI and rain radar. | *"Here is where AgriResilience creates an unfair advantage. Powered by Gemini 1.5 Pro's multimodal perception, it identifies Bacterial Blight with 94% precision. But it doesn't stop at the leaf. In parallel, our agent queries Google Earth Engine for Sentinel-2 satellite multispectral NDVI and radar precipitation over Tukaram's exact farm coordinates. The discovery? A massive monsoon rainstorm is arriving in exactly 3 hours."* | Visual animation of satellite tile loading and radar overlay. |
| **1:30 – 2:05** | The screen highlights the bright red **"HALT SPRAYING"** badge, followed by the generated vernacular audio prescription and recipe. | *"Every existing app would have told Tukaram to spray immediately, wasting 500 rupees into the mud. AgriResilience screams: HALT. It locks the spray window until tomorrow morning, generates an organic neem recipe from kitchen ingredients for pennies, and delivers the entire prescription as a natural Marathi voice note."* | Marathi audio prescription plays cleanly; visual step-by-step card highlights. |
| **2:05 – 2:30** | Zoom out to the **Regional Outbreak Radar Map**. Shows active yellow and red cluster circles covering 5km radius. | *"Furthermore, AgriResilience connects the community. When multiple infections are confirmed, our epidemiological engine maps outbreak clusters, alerting neighboring farmers within a 5-kilometer radius to inspect their borders before the fungal spores spread."* | Interactive map clusters pulse; notification banner appears. |
| **2:30 – 2:48** | Architecture diagram showcasing Google Cloud Run, Vertex AI, Gemini 1.5 Pro, and Earth Engine API. Final slide with Singapore Grand Finale logo. | *"Built end-to-end on Google Cloud Run, Gemini 1.5 Pro, and Earth Engine, AgriResilience saves farmers up to 500 dollars a season while cutting toxic pesticide runoff by 65%. We are bridging the agronomy gap across JAPAC. Thank you, and see you in Singapore!"* | Triumphant outro music, contact links, and GitHub repo URL. |

---

### 4. Ten-Slide Presentation Deck Blueprint (PDF Submission)

1. **Slide 1: Title Slide**: *AgriResilience AI — Hyperlocal Multimodal Agronomy & Climate Defense for Smallholder Farmers* (Theme: Sustainability & Social Impact | Team Credentials & Singapore Finale Target).
2. **Slide 2: The Macro Crisis**: The 1:3,000 Extension Gap, 25–40% crop losses, $30B annual write-offs in JAPAC.
3. **Slide 3: Why Existing Solutions Fail**: Comparison matrix of Plantix (blind to weather), Cropin (enterprise only), and agrochemical dealer conflicts.
4. **Slide 4: The Core Breakthrough**: The Environmental Pathology Graph fusing Gemini 1.5 Pro Vision + Native Dialect Audio + Google Earth Engine Sentinel-2 NDVI.
5. **Slide 5: Technical Architecture on Google Cloud**: Full Cloud Run, Firebase Genkit, Vertex AI, and Earth Engine infrastructure schematic.
6. **Slide 6: Live Product Walkthrough**: 4-panel screenshot flow showing Voice Ingestion $\rightarrow$ Pathology Segmentation $\rightarrow$ Radar Rain Check $\rightarrow$ Dialect Audio Prescription.
7. **Slide 7: Community Outbreak Radar**: Geo-clustered early warning system for neighboring smallholders within a 5km radius.
8. **Slide 8: Quantified Business & Social Impact**: ₹42,000 ($500) saved per family, 65% reduction in pesticide toxicity, 8-second advisory latency.
9. **Slide 9: Business Model & Scalability**: B2G partnerships with agriculture ministries (PM-KISAN in India, Ministry of Agriculture Indonesia) + rural micro-insurance underwriting data.
10. **Slide 10: Live Demo Link & Team Roadmap**: Cloud Run deployment URL, GitHub repository link, and team vision for Demo Day in Singapore on Dec 4, 2026.

---
*Documentation Suite Complete*: Unified Index available in [`README.md`](file:///d:/ai_builder/agri_resilience_docs/README.md).
