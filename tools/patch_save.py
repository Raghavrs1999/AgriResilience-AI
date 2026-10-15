with open('generate_editable_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'output_path = "agri_resilience_docs/AgriResilience_AI_Editable_Pitch_Deck.pptx"',
    'output_path = "agri_resilience_docs/AgriResilience_AI_Master_Editable_Deck.pptx"'
)

with open('generate_editable_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Path replaced!")
