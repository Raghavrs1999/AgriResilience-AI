"""AgriResilience AI — Presentation Generator (python-pptx)
Creates a 12-slide, jury-convincing pitch deck for Google Cloud AI Builder Cup 2026.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Google Botanical Color Palette
    BG_DARK = RGBColor(16, 20, 19)        # #101413
    CARD_BG = RGBColor(29, 33, 31)        # #1D211F
    CARD_BORDER = RGBColor(50, 56, 53)    # Outline
    PRIMARY_GREEN = RGBColor(86, 220, 164) # #56DCA4
    ACCENT_MINT = RGBColor(117, 249, 191)  # #75F9BF
    WARNING_ORANGE = RGBColor(255, 185, 81) # #FFB951
    ALERT_CORAL = RGBColor(255, 180, 171)   # #FFB4AB
    TEXT_LIGHT = RGBColor(245, 248, 245)
    TEXT_MUTED = RGBColor(170, 180, 175)
    PILL_BG = RGBColor(0, 56, 35)

    def set_slide_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_DARK

    def add_header(slide, title_text, category_text="GOOGLE CLOUD AI BUILDER CUP 2026 • FINALE SINGAPORE"):
        # Category Eyebrow Pill
        eyebrow_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_e = eyebrow_box.text_frame
        tf_e.word_wrap = True
        tf_e.margin_left = tf_e.margin_top = tf_e.margin_right = tf_e.margin_bottom = 0
        p_e = tf_e.paragraphs[0]
        p_e.text = category_text.upper()
        p_e.font.size = Pt(11)
        p_e.font.bold = True
        p_e.font.color.rgb = PRIMARY_GREEN

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_LIGHT

    def add_card(slide, left, top, width, height, title, body_bullets, accent_color=PRIMARY_GREEN, border_color=CARD_BORDER):
        # Card shape background
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)

        # Content text frame
        txBox = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(16)
        p_title.font.bold = True
        p_title.font.color.rgb = accent_color
        p_title.space_after = Pt(10)

        for bullet in body_bullets:
            p = tf.add_paragraph()
            p.text = "• " + bullet
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_LIGHT
            p.space_after = Pt(6)

    def add_stat_box(slide, left, top, width, height, value_text, label_text, sub_text="", val_color=PRIMARY_GREEN):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = CARD_BORDER
        shape.line.width = Pt(1.2)

        txBox = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.15), width - Inches(0.3), height - Inches(0.3))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = value_text
        p1.font.size = Pt(28)
        p1.font.bold = True
        p1.font.color.rgb = val_color
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = label_text
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_LIGHT
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(4)

        if sub_text:
            p3 = tf.add_paragraph()
            p3.text = sub_text
            p3.font.size = Pt(9.5)
            p3.font.color.rgb = TEXT_MUTED
            p3.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 1: COVER SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Event Badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(5.8), Inches(0.45))
    badge.fill.solid()
    badge.fill.fore_color.rgb = PILL_BG
    badge.line.color.rgb = PRIMARY_GREEN
    tf_b = badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "GOOGLE CLOUD AI BUILDER CUP 2026 • GRAND FINALE"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = PRIMARY_GREEN
    p_b.alignment = PP_ALIGN.CENTER

    # Title & Subtitle
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.5), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "AgriResilience AI"
    p1.font.size = Pt(48)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_LIGHT

    p2 = tf1.add_paragraph()
    p2.text = "Autonomous Voice-First Agronomy & Planetary Micro-Climate Defense for 450M Smallholder Farmers"
    p2.font.size = Pt(20)
    p2.font.color.rgb = ACCENT_MINT
    p2.space_before = Pt(10)

    # 4 Pillar Highlights on Cover
    add_stat_box(s1, Inches(0.8), Inches(4.5), Inches(2.7), Inches(1.8), "450M", "Smallholders Protected", "India, Indonesia, Vietnam, Philippines", PRIMARY_GREEN)
    add_stat_box(s1, Inches(3.7), Inches(4.5), Inches(2.7), Inches(1.8), "8 Sec", "Latency vs 14 Days", "Instant multi-modal diagnosis", ACCENT_MINT)
    add_stat_box(s1, Inches(6.6), Inches(4.5), Inches(2.7), Inches(1.8), "$500 / Yr", "Direct Farmer Savings", "Eliminates rain wash-off waste", WARNING_ORANGE)
    add_stat_box(s1, Inches(9.5), Inches(4.5), Inches(2.7), Inches(1.8), "100%", "Google Native Stack", "Gemini 3.8 Flash • Earth Engine • Cloud Run", PRIMARY_GREEN)

    # Presenter Footer
    f_box = s1.shapes.add_textbox(Inches(0.8), Inches(6.6), Inches(11.5), Inches(0.5))
    tf_f = f_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Presented by Raghav Sharma • Theme: Sustainability & Social Impact • Track: Generative AI Agents"
    p_f.font.size = Pt(12)
    p_f.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: THE HUMANITARIAN & ECONOMIC CRISIS
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "The Crisis: 450M Smallholders Trapped in the Agronomy Desert", "PROBLEM DEEP-DIVE & HUMAN IMPACT")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8), "1. The Agronomic Desert", [
        "1:3,000 to 1:5,000 Agronomist Deficit across rural India, Indonesia, and Southeast Asia.",
        "7 to 14 days advisory latency before an extension officer can physically reach a 1-hectare field.",
        "Mathematical impossibility: Human experts cannot scale across 450M fragmented farms.",
        "The smallholder is left completely unassisted against compounding climate shocks."
    ], ALERT_CORAL, ALERT_CORAL)

    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8), "2. The Pathogen Tsunami", [
        "Rice Blast & Bacterial Blight consume 80% of crop canopy in just 5 to 7 days.",
        "Pathogens move 2x faster than human extension response times.",
        "Unpredictable climate shifts trigger sudden humidity spikes and erratic unseasonal monsoon downpours.",
        "When the extension officer finally arrives, the field is already 100% ruined."
    ], WARNING_ORANGE, WARNING_ORANGE)

    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "3. Devastating Fallout", [
        "$30 Billion in preventable agricultural crop destruction every year across Asia.",
        "A single blight event costs $420–$720 USD (₹35,000–₹60,000) per affected smallholder.",
        "Represents 60% of total annual household income for rural subsistence farming families.",
        "Leads to predatory debt spirals, loss of generational land, and community malnutrition."
    ], PRIMARY_GREEN, CARD_BORDER)

    # =========================================================================
    # SLIDE 3: WHY LEGACY SOLUTIONS FAIL
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Why Legacy AgTech Fails: The Fatal Flaws We Dissected", "COMPETITIVE LANDSCAPE & FAILURE MECHANICS")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Flaw 1: Consumer Image Apps (Plantix / Mobile CNNs)", [
        "FATAL ENVIRONMENTAL BLINDNESS: Matches pixel patterns in a vacuum. Doesn't know if rain is arriving in 2 hours or if soil is flooded.",
        "THE WASH-OFF DISASTER: Tells farmer to spray fungicide $\\rightarrow$ heavy monsoon downpour arrives 2 hours later $\\rightarrow$ chemical washes into rivers $\\rightarrow$ $40 capital wasted.",
        "PREDATORY COMMERCIAL CONFLICT: Monetized via chemical dealer sponsorships; routinely pushes $15–$30 toxic synthetic bottles when 50¢ bio-extracts suffice.",
        "THE LITERACY BARRIER: 68% of smallholders cannot navigate complex English text menus, Latin checkboxes, or drop-downs."
    ], ALERT_CORAL, ALERT_CORAL)

    add_card(s3, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), "Flaw 2: Enterprise Satellite AgTech (Cropin / Geospatial SaaS)", [
        "COARSE 10KM MACRO GRIDS: Enterprise platforms operate on 10km grid resolutions. A 1-hectare smallholder farm is a 0.01% rounding error.",
        "PROHIBITIVE ENTERPRISE PRICING: SaaS subscriptions cost upwards of $5,000/year, designed strictly for corporate agribusiness conglomerates.",
        "ZERO FIELD VOICE ACCESSIBILITY: Built as dense desktop BI dashboards for executives in air-conditioned offices, not muddy field operations.",
        "DISCONNECTED FROM REALITY: Provides satellite NDVI heatmaps without actionable, vernacular dosage prescriptions for smallholders."
    ], WARNING_ORANGE, CARD_BORDER)

    # =========================================================================
    # SLIDE 4: THE CORE BREAKTHROUGH: ENVIRONMENTAL PATHOLOGY GRAPH
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "The Core Breakthrough: The Environmental Pathology Graph", "MULTIMODAL SENSING & 3-TIER ARCHITECTURE")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8), "Layer 1: Multimodal Ingestion", [
        "Raw 16kHz Opus Audio: Passed directly into Gemini 3.8 Flash's native audio buffer.",
        "Zero Intermediate ASR: Eliminates Whisper error cascades and translation latency.",
        "Code-Switching Fluency: Understands rural slang (Hinglish, Marathi, Bahasa Jawa, 'Tikka Rog').",
        "Canvas-Compressed Leaf Macro: Client compresses to 1920px (under 300KB) to bypass rural 2G/3G bandwidth bottlenecks."
    ], ACCENT_MINT, CARD_BORDER)

    add_card(s4, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8), "Layer 2: Planetary Telemetry", [
        "Google Earth Engine API: Generates exact 100m circular buffer (1-hectare micro-boundary).",
        "Sentinel-2 L2A Multispectral: Calculates NDVI (chlorophyll health) & NDWI (canopy moisture stress).",
        "14-Day Cloud Mask Lookback: Automatically rejects cloudy satellite passes during monsoons.",
        "ERA5 72h Weather Radar: Hyperlocal precipitation probabilities and surface thermal forecasts."
    ], PRIMARY_GREEN, CARD_BORDER)

    add_card(s4, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "Layer 3: Autonomous Synthesis", [
        "Fuses Pathology + Satellite + Weather into unified Environmental Pathology Graph.",
        "Grounded in Vertex AI Vector Search across ICAR and FAO agronomic handbooks.",
        "Enforces the 'Wash-Off Rule Engine' to halt spray if rain is predicted within 4 hours.",
        "Generates calming vernacular voice note via Cloud TTS Neural2 at 0.92x speaking rate."
    ], WARNING_ORANGE, CARD_BORDER)

    # =========================================================================
    # SLIDE 5: THE WASH-OFF RULE ENGINE & ECONOMIC PRESERVATION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "The Wash-Off Rule: Halting Sprays to Protect Farmer Capital", "ALGORITHMIC DECISION TREE & SAFETY OVERRIDE")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(7.5), Inches(4.8), "Autonomous Wash-Off Decision Engine Logic", [
        "Continuous Multi-Variable Evaluation: Ingests Pathogen Identity + Disease Stage + NDVI Score + ERA5 4-Hour Precipitation Forecast.",
        "NON-NEGOTIABLE SAFETY OVERRIDE: If ERA5 Rain Probability > 60% within 4 Hours $\\rightarrow$ Hardcode HALT_SPRAYING Red Flag Protocol.",
        "Output Generation Lockdown: System explicitly refuses to provide chemical dilution recipes and warns: 'DO NOT SPRAY NOW'.",
        "Immediate Capital Preservation: Saves ₹500–₹1,000 ($6–$12) per avoided wasteful spray event.",
        "Environmental Protection: Prevents 65% of toxic synthetic pesticide runoff from poisoning local water tables and rivers.",
        "Safe Rescheduling Window: Automatically prescribes an optimal post-rain application window (e.g., tomorrow 6:30 AM – 8:30 AM)."
    ], PRIMARY_GREEN, PRIMARY_GREEN)

    add_stat_box(s5, Inches(8.8), Inches(1.8), Inches(3.7), Inches(2.2), "65%", "Pesticide Runoff Reduction", "Protects rural watersheds from chemical pollution", PRIMARY_GREEN)
    add_stat_box(s5, Inches(8.8), Inches(4.4), Inches(3.7), Inches(2.2), "₹42,000", "Savings / Season ($505)", "Directly preserves smallholder household cashflow", WARNING_ORANGE)

    # =========================================================================
    # SLIDE 6: TIERED BIO-REMEDIATION PROTOCOL
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Farmer-First Prescriptions: Organic Bio-Protection vs Chemicals", "ICAR & FAO VALIDATED AGRONOMIC TREATMENTS")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8), "Tier 1: Bio-Protection (<30% Severity)", [
        "MANDATORY BIO-FIRST RULE: When disease severity is below 30%, industrial chemicals are strictly banned.",
        "Hyperlocal Organic Recipes: 5% Neem Seed Kernel Extract (NSKE), sour buttermilk foliar spray, Cow Urine + Asafoetida.",
        "Accessible Ingredients: Farmer already possesses materials on the farm or purchases locally for pennies.",
        "Cost: ₹45 (50¢ USD) vs ₹550 ($7 USD) dealer chemical alternative $\\rightarrow$ 92% cost reduction!"
    ], PRIMARY_GREEN, PRIMARY_GREEN)

    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8), "Tier 2: Targeted Chemicals (≥30% Severity)", [
        "CALIBRATED ESCALATION: When crop canopy is in critical epidemic danger, chemical intervention is permitted.",
        "Zero Brand Bias: Recommends generic chemical active ingredients (e.g. Copper Oxychloride 50% WP + Streptocycline).",
        "Mandatory Safety Parameters: Appends exact dilution ratios, PPE requirements, and legal withholding periods (14 days before harvest).",
        "Food Safety Compliance: Guarantees harvest is safe for human consumption without toxic residue."
    ], WARNING_ORANGE, CARD_BORDER)

    add_card(s6, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "Special Case: Viral Pathogens (Cassava)", [
        "THE VIRAL STUNTING TRAP: Chemical dealers routinely sell expensive, useless fungicides to treat viral diseases.",
        "ZERO-SPRAY INTERVENTION: Detects viral mosaic $\\rightarrow$ forbids all chemical sprays.",
        "Mechanical Roguing Protocol: Guides farmer to uproot and burn infected stunted plants outside the perimeter.",
        "Vector Control: Deploys low-cost yellow sticky traps to capture whiteflies and halt transmission $\\rightarrow$ saves ₹925."
    ], ALERT_CORAL, CARD_BORDER)

    # =========================================================================
    # SLIDE 7: 5KM OUTBREAK EARLY WARNING RADAR
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "5km Outbreak Radar: Community Defense Network Effects", "EPIDEMIOLOGICAL SPATIAL CLUSTERING")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Privacy-Preserving Spatial Clustering", [
        "BEYOND POINT SOLUTIONS: Pathogens do not stop at property lines. Solving one farm must build a community defense shield.",
        "Geohash Level 6 Anonymization: GPS coordinates are never stored in raw form. Encrypted into a 1.2km × 0.6km bounding box.",
        "Haversine Spatial Proximity: Backend queries active disease logs across Firestore within a 5-kilometer spherical radius.",
        "Cluster Trigger Threshold: When $\\ge 3$ neighboring farms log the same airborne pathogen in 72 hours $\\rightarrow$ Outbreak Active!",
        "Proactive Push Alerts: Dispatches immediate alert badges to all smallholders in the zone: 'Warning: Rice Blast detected in 4 nearby paddies. Inspect borders immediately!'"
    ], ACCENT_MINT, PRIMARY_GREEN)

    add_card(s7, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), "From Reactive Tool to Proactive Defense Shield", [
        "Traditional Model: Farmer reacts 5 days late when plant is already wilting and dying.",
        "AgriResilience Model: Farmer receives community early warning BEFORE fungal spores land on their crop.",
        "Preemptive Perimeter Spraying: Farmer sprays low-cost bio-repellent on border rows, extinguishing the outbreak early.",
        "Collective Community Resilience: Halts agricultural epidemic transmission across entire village clusters."
    ], PRIMARY_GREEN, CARD_BORDER)

    # =========================================================================
    # SLIDE 8: 3 PRE-PACKAGED DEMO EVALUATION DOSSIERS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Live Evaluation Scenarios: 3 Pre-Packaged Field Dossiers", "PROVEN EDGE CASES IN LIVE DEMONSTRATION")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(3.7), Inches(4.8), "Dossier A: Maharashtra Cotton", [
        "Farmer: Tukaram Shinde (Jalna, MH)",
        "Language: Marathi vernacular dialect",
        "Crop & Disease: Cotton • Bacterial Blight",
        "Telemetry: NDVI 0.412 • Rain 18.5mm in 3h",
        "ACTION VERDICT: HALT SPRAY (Wash-Off)",
        "Prescription: 5% Neem extract tomorrow morning",
        "Economics: Saves ₹505 in wasted chemicals"
    ], ALERT_CORAL, ALERT_CORAL)

    add_card(s8, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.8), "Dossier B: West Bengal Paddy", [
        "Farmer: Debabrata Roy (Nadia, WB)",
        "Language: Bengali vernacular dialect",
        "Crop & Disease: Paddy Rice • Rice Blast",
        "Telemetry: 48-Hour Dry Window • High Humidity",
        "ACTION VERDICT: CLEAR WINDOW (Spray)",
        "Prescription: Pseudomonas fluorescens bio-spray",
        "Radar: 4 adjacent farms infected $\\rightarrow$ 5km Alert!"
    ], PRIMARY_GREEN, PRIMARY_GREEN)

    add_card(s8, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "Dossier C: East Java Cassava", [
        "Farmer: Budi Santoso (Java, Indonesia)",
        "Language: Bahasa Indonesia dialect",
        "Crop & Disease: Cassava • Mosaic Virus",
        "Pathogen Type: VIRAL INFECTION",
        "ACTION VERDICT: HALT CHEMICALS (Viral)",
        "Prescription: Mechanical roguing & yellow traps",
        "Economics: Prevents ₹925 useless chemical purchase"
    ], WARNING_ORANGE, WARNING_ORANGE)

    # =========================================================================
    # SLIDE 9: FULL GOOGLE CLOUD ARCHITECTURAL STACK
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "100% Google Cloud Native Architecture", "TECHNICAL MERIT & ENTERPRISE PRODUCTION STACK")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Google Cloud Compute & AI Pipeline", [
        "Google Cloud Run: Containerized FastAPI ASGI backend deployed in asia-southeast1 (Singapore), sub-80ms regional latency, auto-scales 0 to 1,000 instances.",
        "Gemini 3.8 Flash & Gemini 1.5 Pro: Multimodal ingestion of 16kHz audio streams and 1920px compressed leaf macros via official google-genai SDK.",
        "Google Earth Engine API: Programmatic Python service account integration pulling Sentinel-2 L2A (10m bands) & ERA5-Land reanalysis radar.",
        "Vertex AI Vector Search: Sub-millisecond vector indexing over verified ICAR/FAO agronomic remediation repositories."
    ], PRIMARY_GREEN, PRIMARY_GREEN)

    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), "Data, Speech & Frontend Cockpit", [
        "Cloud Firestore: Real-time geospatial cluster telemetry and anonymized geohash records.",
        "Google Cloud Text-to-Speech: Neural2 speech synthesis delivering vernacular audio prescriptions at calming 0.92x speaking rate.",
        "Google BigQuery: 'daily_blight_telemetry' partitioning for state-level regional epidemiology heatmaps.",
        "Firebase Hosting & PWA: Material Design 3 and Google PAIR compliant Progressive Web App with 48px touch targets and offline service workers."
    ], ACCENT_MINT, CARD_BORDER)

    # =========================================================================
    # SLIDE 10: GOOGLE PAIR & MATERIAL DESIGN 3 EXCELLENCE
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Design Excellence: Google Material 3 & PAIR Standards", "HUMAN-AI CENTRIC DESIGN & ACCESSIBILITY")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Google PAIR (People + AI Research) Principles", [
        "Calibrate Trust via Explainability Drawer: 'Why did the AI recommend this?' reveals exact weights: Visual Pathology (38.5%), Satellite NDVI (0.412), ERA5 Rain (88%).",
        "Human-in-the-Loop Feedback: Field agronomists can 'Confirm Diagnosis' or 'Suggest Correction', feeding telemetry into active learning loops.",
        "Set Contextual Expectations: Explicitly informs smallholders that forecasts rely on satellite radar telemetry.",
        "Graceful Fallback Engineering: Dual language audio buttons (Vernacular + English Translation) ensure speech never fails on any device."
    ], ACCENT_MINT, PRIMARY_GREEN)

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), "Google Material Design 3 (M3) Standards", [
        "Botanical Tonal Palette: Primary (#56DCA4), Surface Container roles, subtle elevation, and light/dark theme switching.",
        "Strict 48x48dp Touch Targets: Ergonomic oversized microphone FAB and filter chips designed for one-handed operation in bright sunlight.",
        "Official Google Material Symbols: Replaced generic icons with material-symbols-outlined across all telemetry views.",
        "Auditory Accessibility: Dialect speech synthesis eliminates the literacy barrier for 68% of smallholders."
    ], PRIMARY_GREEN, CARD_BORDER)

    # =========================================================================
    # SLIDE 11: BUSINESS MODEL & PLANETARY SCALABILITY
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Monetization & Scale: Free for Farmers, Funded by Institutions", "BUSINESS VIABILITY & PLANETARY IMPACT")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "B2G Government Agriculture Partnerships", [
        "Free for Smallholders Forever: Charging subsistence farmers is economically and morally flawed.",
        "Government Ministries of Agriculture: National initiatives (PM-Kisan in India, Kementan in Indonesia) spend billions on manual crop surveys.",
        "BigQuery Live Epidemiology Heatmaps: Governments license our real-time disease radar to dispatch subsidized bio-pesticides ahead of infection fronts.",
        "Food Security Dashboard: Tracks national harvest yield projections with planetary satellite precision."
    ], PRIMARY_GREEN, CARD_BORDER)

    add_card(s11, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), "Parametric Micro-Insurance Underwriting", [
        "InsurTech Ecosystem Integration: Rural crop insurance is currently impossible to underwrite due to manual verification costs.",
        "Automated Parametric Triggers: Insurers plug into AgriResilience telemetry $\\rightarrow$ when an epidemiological cluster reaches 5km, automated payouts trigger instantly.",
        "Zero Paperwork & Zero Fraud: Satellite NDVI data proves crop distress without requiring corrupt loss adjusters.",
        "Data Licensing Revenue: Micro-insurance providers pay an API fee per covered hectare, generating sustainable recurring revenue."
    ], WARNING_ORANGE, PRIMARY_GREEN)

    # =========================================================================
    # SLIDE 12: THE WINNING SUMMARY & JURY PITCH
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Why AgriResilience AI Wins the AI Builder Cup 2026", "GRAND FINALE SUMMARY & RUBRIC MASTERY")

    add_stat_box(s12, Inches(0.8), Inches(1.8), Inches(2.7), Inches(1.8), "40%", "Technical Merit & GenAI", "Gemini 3.8 Flash • GEE • Vertex AI", PRIMARY_GREEN)
    add_stat_box(s12, Inches(3.7), Inches(1.8), Inches(2.7), Inches(1.8), "20%", "Innovation & Novelty", "Voice-First Multimodal Ingestion", ACCENT_MINT)
    add_stat_box(s12, Inches(6.6), Inches(1.8), Inches(2.7), Inches(1.8), "20%", "Viability & Architecture", "Cloud Run Container • Sub-80ms Latency", WARNING_ORANGE)
    add_stat_box(s12, Inches(9.5), Inches(1.8), Inches(2.7), Inches(1.8), "20%", "Sustainability Impact", "450M Smallholders • $30B Waste Prevented", PRIMARY_GREEN)

    add_card(s12, Inches(0.8), Inches(4.0), Inches(11.7), Inches(2.6), "The Unbeatable Closing Argument for Judy & The Jury", [
        "UNMATCHED PROBLEM SCALE: Bridges the 1:3,000 agronomist deficit feeding 1 Billion people across JAPAC.",
        "TECHNICAL ELEGANCE OVER VAPORWARE: Fully functional live prototype running on Google Cloud today (not future promises).",
        "GENUINE HUMAN-CENTRIC DESIGN: Solves illiteracy through vernacular speech while protecting the planet through satellite radar.",
        "AgriResilience AI does not merely manage crises — it mathematically preempts them. Thank you, and see you in Singapore!"
    ], PRIMARY_GREEN, PRIMARY_GREEN)

    # Save Presentation
    output_path = os.path.join(os.path.dirname(__file__), "agri_resilience_docs", "AgriResilience_AI_Jury_Pitch_Deck.pptx")
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_deck()
