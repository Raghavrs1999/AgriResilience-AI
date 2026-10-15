"""AgriResilience AI — Authentic Human Vernacular Voice Synthesizer

Uses Google Text-to-Speech (gTTS) to synthesize real, fluent, human-understandable
voice notes and clinical prescriptions across all target JAPAC vernacular languages.
"""

import os
import shutil
from gtts import gTTS

BACKEND_AUDIO_DIR = r"d:\ai_builder\backend\data\audio"
FRONTEND_AUDIO_DIR = r"d:\ai_builder\frontend\assets\audio"

os.makedirs(BACKEND_AUDIO_DIR, exist_ok=True)
os.makedirs(FRONTEND_AUDIO_DIR, exist_ok=True)

# 1. Authentic Farmer Consultation Voice Notes (Input Notes)
INPUT_VOICE_NOTES = [
    {
        "filename": "cotton_blight_mr_16k.mp3",
        "wav_alias": "cotton_blight_mr_16k.wav",
        "lang": "mr",
        "text": "साहेब, आमच्या कपाशीच्या पानांवर काळे-तांबडे डाग पडले आहेत आणि झाड सुकत चाललंय. काय फवारणी करू?",
        "desc": "Marathi - Cotton Bacterial Blight"
    },
    {
        "filename": "rice_blast_bn_16k.mp3",
        "wav_alias": "rice_blast_bn_16k.wav",
        "lang": "bn",
        "text": "ধান গাছের পাতায় নৌকার মতো চোখের দাগ হয়েছে। পুরো মাঠ নষ্ট হয়ে যাবে মনে হচ্ছে। কি ওষুধ দেব?",
        "desc": "Bengali - Paddy Rice Blast"
    },
    {
        "filename": "cassava_cmd_id_16k.mp3",
        "wav_alias": "cassava_cmd_id_16k.wav",
        "lang": "id",
        "text": "Daun singkong saya menguning keriting dan batangnya kerdil. Ini kena penyakit apa ya pak?",
        "desc": "Bahasa Indonesia - Cassava Mosaic"
    },
    {
        "filename": "maize_blight_te_16k.mp3",
        "wav_alias": "maize_blight_te_16k.wav",
        "lang": "te",
        "text": "అయ్యా, మొక్కజొన్న ఆకులపై పెద్ద మచ్చలు పడ్డాయి, పురుగులు ఆకులను తినేస్తున్నాయి. వెంటనే ఏం మందు కొట్టాలి?",
        "desc": "Telugu - Maize Blight & Armyworm"
    },
    {
        "filename": "sugarcane_redrot_ta_16k.mp3",
        "wav_alias": "sugarcane_redrot_ta_16k.wav",
        "lang": "ta",
        "text": "ஐயா, கரும்பு தண்டுக்குள் சிவப்பு நிறமாக மாறி நாற்றம் அடிக்கிறது. பயிர் முழுவதும் காய்கிறது. என்ன செய்வது?",
        "desc": "Tamil - Sugarcane Red Rot"
    },
    {
        "filename": "wheat_rust_hi_16k.mp3",
        "wav_alias": "wheat_rust_hi_16k.wav",
        "lang": "hi",
        "text": "बाबूजी, गेहूं की पत्तियों पर पीली-पीली हल्दी जैसी धारियां बन गई हैं। हाथ लगाने पर पीला पाउडर छूट रहा है।",
        "desc": "Hindi - Wheat Stripe Rust"
    },
    {
        "filename": "soybean_rust_vi_16k.mp3",
        "wav_alias": "soybean_rust_vi_16k.wav",
        "lang": "vi",
        "text": "Thưa chuyên gia, mặt dưới lá đậu nành có nhiều đốm nhỏ li ti màu nâu đỏ như rỉ sắt, lá đang rụng nhiều. Tôi nên phun thuốc gì?",
        "desc": "Vietnamese - Soybean Asian Rust"
    },
]

# 2. Prescription Audio Advisories (Output Notes)
PRESCRIPTION_VOICE_NOTES = [
    {
        "filename": "rx_cotton_blight_mr.mp3",
        "lang": "mr",
        "text": "नमस्कार तुकारामजी. तुमच्या कपाशीवर जिवाणू करपा रोगाचा प्रादुर्भाव झाला आहे. महत्त्वाची सूचना: आज लगेच कोणतीही औषध फवारणी करू नका! सॅटेलाइट रडारनुसार पुढच्या ३ तासांत जोरदार पाऊस येणार असून औषध वाहून जाईल. उद्या सकाळी पाच टक्के निंबोळी अर्क फवारा. यामुळे तुमचे ५०० रुपये वाचतील.",
        "desc": "Marathi Rx - Halt Spraying Rain Advisory"
    },
    {
        "filename": "rx_rice_blast_bn.mp3",
        "lang": "bn",
        "text": "নমস্কার দেবব্রতবাবু। আপনার ধানে ব্লাস্ট রোগের লক্ষণ নিশ্চিত হয়েছে। আগামী ৪৮ ঘণ্টা বৃষ্টির কোনো সম্ভাবনা নেই। তাই অবিলম্বে আজ বিকেলেই সিউডোমোনাস ফ্লোরোসেন্স স্প্রে করুন।",
        "desc": "Bengali Rx - Safe to Spray Advisory"
    },
    {
        "filename": "rx_cassava_cmd_id.mp3",
        "lang": "id",
        "text": "Halo Pak Budi. Tanaman singkong bapak terserang virus mozaik. Jangan beli obat semprot fungisida kimia karena virus tidak bisa sembuh dengan semprotan. Segera cabut dan bakar batang singkong yang kerdil, lalu pasang perangkap kuning untuk kutu kebul.",
        "desc": "Bahasa Indonesia Rx - Rogue Plants Viral Advisory"
    },
    {
        "filename": "rx_maize_blight_te.mp3",
        "lang": "te",
        "text": "నమస్కారం వెంకటరావు గారు. మీ మొక్కజొన్న పైరుపై ఆకుమచ్చ తెగులు ఆశించింది. రాబోయే 3 గంటల్లో భారీ వర్షం పడే సూచన ఉంది, కాబట్టి ఈరోజు ఎలాంటి మందులు పిచికారీ చేయవద్దు. రేపు ఉదయం జీవ నియంత్రణ మందులు చల్లండి.",
        "desc": "Telugu Rx - Rain Halt Advisory"
    },
    {
        "filename": "rx_sugarcane_redrot_ta.mp3",
        "lang": "ta",
        "text": "வணக்கம் திரு முருகன். உங்கள் கரும்பில் செவ்வழுகல் நோய் தாக்கியுள்ளது. பாதிக்கப்பட்ட கரும்புகளை உடனடியாக வேரோடு பிடுங்கி தீயிட்டு அழிக்கவும். டிரைக்கோடெர்மா கரைசலை வேர்ப் பகுதியில் ஊற்றவும்.",
        "desc": "Tamil Rx - Bio-drench Advisory"
    },
    {
        "filename": "rx_wheat_rust_hi.mp3",
        "lang": "hi",
        "text": "राम-राम बलवंत जी। आपके गेहूं में पीला रतुआ आ चुका है। मौसम बिल्कुल साफ है और तीन दिनों तक बारिश नहीं होगी। आज ही दोपहर में ओस सूखने के बाद प्रोपिकोनाज़ोल का छिड़काव तुरंत करें।",
        "desc": "Hindi Rx - Clear Weather Spray Advisory"
    },
    {
        "filename": "rx_soybean_rust_vi.mp3",
        "lang": "vi",
        "text": "Chào bác Hải. Cây đậu nành của bác bị bệnh rỉ sắt Châu Á. Cảnh báo khẩn cấp: 2 giờ nữa sẽ có mưa to 22mm, tuyệt đối không được phun thuốc hôm nay. Bác hãy đợi sáng mai trời ráo rồi phun thuốc.",
        "desc": "Vietnamese Rx - Monsoon Wash-off Advisory"
    },
]

def synthesize_all():
    print("=" * 65)
    print("  SYNTHESIZING AUTHENTIC HUMAN VERNACULAR VOICE NOTES (gTTS)")
    print("=" * 65)
    
    # Synthesize Inputs
    print("\n>>> [1/2] Farmer Input Consultation Audio Notes:")
    for item in INPUT_VOICE_NOTES:
        mp3_backend = os.path.join(BACKEND_AUDIO_DIR, item["filename"])
        wav_alias_backend = os.path.join(BACKEND_AUDIO_DIR, item["wav_alias"])
        mp3_frontend = os.path.join(FRONTEND_AUDIO_DIR, item["filename"])
        wav_alias_frontend = os.path.join(FRONTEND_AUDIO_DIR, item["wav_alias"])
        
        tts = gTTS(text=item["text"], lang=item["lang"], slow=False)
        tts.save(mp3_backend)
        # Duplicate to frontend
        shutil.copy2(mp3_backend, mp3_frontend)
        # Also copy as .wav alias so any legacy .wav references play cleanly
        shutil.copy2(mp3_backend, wav_alias_backend)
        shutil.copy2(mp3_backend, wav_alias_frontend)
        
        size_kb = os.path.getsize(mp3_backend) / 1024
        print(f"  [OK] {item['desc']} -> {item['filename']} ({size_kb:.1f} KB)")
        
    # Synthesize Prescription Outputs
    print("\n>>> [2/2] Agronomic Prescription Audio Advisories:")
    for item in PRESCRIPTION_VOICE_NOTES:
        mp3_backend = os.path.join(BACKEND_AUDIO_DIR, item["filename"])
        mp3_frontend = os.path.join(FRONTEND_AUDIO_DIR, item["filename"])
        
        tts = gTTS(text=item["text"], lang=item["lang"], slow=False)
        tts.save(mp3_backend)
        shutil.copy2(mp3_backend, mp3_frontend)
        
        size_kb = os.path.getsize(mp3_backend) / 1024
        print(f"  [OK] {item['desc']} -> {item['filename']} ({size_kb:.1f} KB)")
        
    print("\n" + "=" * 65)
    print("  ALL VERNACULAR HUMAN AUDIO NOTES SUCCESSFULLY SYNTHESIZED!")
    print("=" * 65)

if __name__ == "__main__":
    synthesize_all()
