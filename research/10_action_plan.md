# Deliverable 10: Action Plan
## Tactical 7-Day Sprint Plan: From Research to Winning Hackathon Submission

> **Timeline Window**: October 11, 2026 → October 18, 2026 (Submission Deadline: 11:59 PM SGT)  
> **Mandatory Submissions**:
> 1. Working Prototype deployed live on **Google Cloud Run** and **Firebase Hosting**
> 2. 3-Minute Video Demonstration link (YouTube / Vimeo / Google Drive)
> 3. Proposal Presentation Deck (PDF format, max 10–12 slides)
> 4. Public GitHub Repository with complete documentation and architecture diagrams

---

### 1. Day-by-Day Tactical Execution Roadmap

```
  DAY 1 (Oct 11)        DAY 2 (Oct 12)        DAY 3 (Oct 13)        DAY 4 (Oct 14)
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Synthetic Data  │──▶│ Multi-Agent Core│──▶│ API Tool Calling│──▶│ Frontend UI &   │
│ & Validation    │   │ (Vertex/Gemini) │   │ & Graph Engine  │   │ Visual Cockpit  │
└─────────────────┘   └─────────────────┘   └─────────────────┘   └─────────────────┘
                                                                           │
                                                                           ▼
  DAY 7 (Oct 17-18)     DAY 6 (Oct 16)        DAY 5 (Oct 15)               │
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐            │
│ Final Packaging │◀──│ Video Demo &    │◀──│ Cloud Run /     │◀───────────┘
│ & Submission    │   │ Deck Production │   │ Firebase Deploy │
└─────────────────┘   └─────────────────┘   └─────────────────┘
```

---

#### Day 1 (Oct 11): Synthetic Trade Corpus Generation & Sanity Validation
- **Objective**: Generate authentic, realistic test datasets representing the 3 core evaluation scenarios.
- **Key Tasks**:
  1. Build `generate_trade_corpus.py` using Python (`reportlab` / `fpdf2` / `Pillow`) to generate high-resolution PDF documents:
     - Scenario 1 (Legitimate): Clean electronics shipment (Singapore → Nhava Sheva, India).
     - Scenario 2 (Document Forgery): Tampered rubber customs stamp, altered invoice amount, duplicate container checksum.
     - Scenario 3 (Ghost Shipment & Shell Ring): Shell companies in Jakarta, Singapore, and Mumbai trading phantom palm oil.
  2. Implement simulated external registries:
     - Mock AIS Marine Vessel Tracking endpoint (`/api/vessel/verify`).
     - Mock Sanctions & Watchlist registry (`/api/sanctions/screen`).
     - Mock Inter-Bank Duplicate Invoice Hash registry (`/api/invoices/check-hash`).

---

#### Day 2 (Oct 12): Agentic Backend Engine (Vertex AI & Gemini 1.5)
- **Objective**: Build the autonomous multi-agent reasoning pipeline in Python FastAPI.
- **Key Tasks**:
  1. Set up Google Cloud project with Vertex AI and Gemini 1.5 Flash/Pro API keys.
  2. Implement **Agent 1: Ingestion & Forensic Document Vision Agent**:
     - Sends full PDF pages to Gemini 1.5 Flash with structured JSON schemas.
     - Extracts entities: Importer, Exporter, Bill of Lading Number, Container ID, Ports, Amount, Currency, Incoterms.
     - Performs visual stamp & pixel tampering detection.
  3. Implement **Agent 2: Entity Reconciliation & Cross-Validation Agent**:
     - Cross-checks entity consistency across Bill of Lading, Invoice, and Letter of Credit.
     - Flags mathematical mismatches (e.g., unit price × quantity ≠ total invoice value).

---

#### Day 3 (Oct 13): Graph Ring Intelligence & SAR Generation
- **Objective**: Complete multi-hop collusion detection and automated regulatory reporting.
- **Key Tasks**:
  1. Implement **Agent 3: Circular Trade & Network Graph Agent**:
     - Uses Python `networkx` to build an in-memory graph of corporate entities, directors, bank accounts, and addresses.
     - Runs cycle detection algorithms (`simple_cycles`) to flag circular trade loops.
  2. Implement **Agent 4: Audit & SAR Synthesis Agent**:
     - Ingests outputs from Agents 1, 2, and 3 into Gemini 1.5 Pro.
     - Computes a weighted Composite Risk Score (0–100).
     - Automatically generates a formatted, regulatory-grade PDF Suspicious Activity Report (SAR) with evidence citations.

---

#### Day 4 (Oct 14): Interactive "Investigation Cockpit" Frontend
- **Objective**: Build a visually stunning, high-contrast web dashboard that captivates judges in the first 10 seconds.
- **Key Tasks**:
  1. Initialize React + Vite project with TailwindCSS and Lucide-react icons.
  2. Design the three core views:
     - **Triage Dashboard**: Live stats (Packets Analyzed, Fraud Volume Prevented, Flagged Ratio) and quick-load demo dossiers.
     - **Deep Forensic Workspace**: Side-by-side document viewer showing bounding box overlays on tampered text and forged rubber stamps.
     - **Interactive Network Graph**: Visual graph (using `vis-network` or `force-graph`) showing buyer-seller-director circular loops.
  3. Add animated live agent streaming: visual checklist showing agents executing in real time with status badges.

---

#### Day 5 (Oct 15): Cloud Deployment & End-to-End Testing (Cloud Run & Firebase)
- **Objective**: Deploy production containers on Google Cloud infrastructure per hackathon rules.
- **Key Tasks**:
  1. Containerize the FastAPI backend via `Dockerfile` and deploy to **Google Cloud Run**:
     ```bash
     gcloud run deploy trustshield-backend \
       --source . \
       --region asia-southeast1 \
       --allow-unauthenticated
     ```
  2. Build and deploy the React frontend to **Firebase Hosting**:
     ```bash
     firebase deploy --only hosting
     ```
  3. Run comprehensive stress tests: verify that document analysis completes in under 15 seconds with zero API rate-limit errors.

---

#### Day 6 (Oct 16): 3-Minute Video Production & Presentation Deck
- **Objective**: Produce the pitch deck and live demonstration video according to official guidelines.
- **Key Tasks**:
  1. **Pitch Deck (10 Slides in PDF)**:
     - Slide 1: Title & JAPAC Context (TrustShield JAPAC: AI Trade Fraud Defense)
     - Slide 2: The Problem ($14B Trade Finance Fraud Gap in Asia)
     - Slide 3: Why Existing Tools Fail (Hash registries miss synthetic tampering)
     - Slide 4: Solution Overview (Autonomous Multi-Agent Architecture)
     - Slide 5: Deep Technical Architecture on Google Cloud (Gemini 1.5 + Cloud Run)
     - Slide 6: Live Demo Walkthrough (Side-by-side forensic analysis)
     - Slide 7: Measurable Business Impact (72 hrs → 12 secs; 99% cost reduction)
     - Slide 8: Market Opportunity & TAM/SAM in JAPAC
     - Slide 9: Team Credentials & Execution Roadmap
     - Slide 10: Conclusion & Grand Finale Vision
  2. **3-Minute Demo Video Recording**:
     - *0:00 – 0:35*: The Hook & Problem (Showcase the massive paper mountain in Asian ports and news clips of multimillion-dollar duplicate financing scandals).
     - *0:35 – 2:05*: Live Screen Recording of the Working Prototype on Cloud Run (Upload Dossier C; watch agents flag the forged stamp, detect the ghost vessel in Rotterdam, and expose the circular shell ring on the interactive graph).
     - *2:05 – 2:40*: Technical Architecture & Google Cloud Integration (Walk through Gemini 1.5 1M context, Vertex AI Agent Builder, and Cloud Run deployment).
     - *2:40 – 3:00*: Impact Metrics & Call to Action (Singapore Grand Finale readiness).
  3. Upload video to YouTube (Unlisted, 1080p 60fps) or Google Drive with public view permissions.

---

#### Day 7 (Oct 17–18): Final Audit, Documentation & Formal Submission
- **Objective**: Review all submission requirements against Hack2skill rules and finalize entry.
- **Submission Checklist**:
  - [ ] **Working Cloud Run / Firebase URL**: Tested and accessible globally with no authentication barriers.
  - [ ] **Demo Video**: Working link, clear audio, under 3 minutes (e.g., 2m 55s), 1080p HD.
  - [ ] **Presentation Deck**: Exported as clean PDF (<20MB).
  - [ ] **GitHub Repository**: Clean README with architecture diagrams, setup instructions, and Google Cloud usage disclosures.
  - [ ] **Hack2skill Portal Submission**: Completed before deadline (Oct 18, 2026, 11:59 PM SGT).

---

### 2. Risk Matrix & Contingency Controls

| Potential Risk | Severity | Probability | Mitigation Strategy |
| :--- | :---: | :---: | :--- |
| **Vertex AI API Rate Limits during live testing** | High | Low | Cache parsed responses for standard demo dossiers; implement exponential backoff with Gemini 1.5 Flash fallback. |
| **Cloud Run cold start latency (>5 seconds)** | Moderate | Moderate | Configure `--min-instances 1` during the judging evaluation window (Oct 19–Nov 6) to guarantee instant responses. |
| **PDF parsing failure on corrupted file uploads** | Moderate | Low | Sanitize input files using PyMuPDF before passing image buffers to Gemini Vision. |
| **Video exceeds 3-minute hard cutoff** | High | Low | Script video word-for-word (max 380 spoken words) and edit tightly to exactly 2:50. |

---
*Deliverable Series Complete*: Review the synthesized master overview in [`research_results.md`](file:///d:/ai_builder/research_results.md).
