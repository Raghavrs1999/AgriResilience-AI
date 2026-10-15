"""Update HTML pitch decks to offer both Editable PPTX and Visual PPTX download links"""

for path in ['frontend/pitch_deck.html', 'agri_resilience_docs/pitch_deck.html']:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    old_btn = '''<a class="btn-header" href="/agri_resilience_docs/AgriResilience_AI_Jury_Pitch_Deck.pptx" download>
        <span class="material-symbols-outlined" style="font-size:16px;">download</span>
        Download .pptx
      </a>'''

    new_btns = '''<a class="btn-header" href="/agri_resilience_docs/AgriResilience_AI_Editable_Pitch_Deck.pptx" download style="border-color:var(--primary); color:var(--primary);" title="100% Native Shapes and Text (88 KB)">
        <span class="material-symbols-outlined" style="font-size:16px;">edit_note</span>
        Editable PPTX (88 KB)
      </a>
      <a class="btn-header" href="/agri_resilience_docs/AgriResilience_AI_Jury_Pitch_Deck.pptx" download title="Cinematic 2K Visual Plates (38 MB)">
        <span class="material-symbols-outlined" style="font-size:16px;">photo_library</span>
        Visual PPTX (38 MB)
      </a>'''

    if old_btn in html:
        html = html.replace(old_btn, new_btns)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {path} with both download links.")
    else:
        print(f"Old button not found in {path}")
