for path in ['frontend/pitch_deck.html', 'agri_resilience_docs/pitch_deck.html']:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace(
        'AgriResilience_AI_Master_Editable_Deck.pptx',
        'AgriResilience_AI_Executive_Presentation.pptx'
    )
    html = html.replace(
        'AgriResilience_AI_Editable_Pitch_Deck.pptx',
        'AgriResilience_AI_Executive_Presentation.pptx'
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated link in {path}")
