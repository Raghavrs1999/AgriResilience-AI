with open("build_clean_deck.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(
    'out_path = "agri_resilience_docs/AgriResilience_AI_Master_Editable_Deck.pptx"',
    'out_path = "agri_resilience_docs/AgriResilience_AI_Executive_Presentation.pptx"'
)

with open("build_clean_deck.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated output path to AgriResilience_AI_Executive_Presentation.pptx")
