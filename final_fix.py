import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# Fix Image Containers for Slide 4, 5, 6
# I will change the image-container div to display: block and text-align: center so the image renders normally.
# And add a fallback width just in case.

def fix_image_container(slide_num, alt_text, expected_src, errors_array):
    old_pattern = r'<div class="image-container" style="margin: 2rem auto; width: 100%; justify-content: center;">\s*<img src="([^"]+)" alt="' + alt_text + r'" style="max-height: 50vh; cursor: pointer;" onclick="openImageModal\([^)]+\)">\s*</div>'
    new_html = f"""<div class="image-container" style="display: block; text-align: center; margin: 2rem auto;">
                <img src="{expected_src}" alt="{alt_text}" style="max-height: 50vh; max-width: 100%; width: auto; object-fit: contain; cursor: pointer; border-radius: 1.2rem; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6);" onclick="openImageModal(this.src, this.src, {errors_array})">
            </div>"""
    return re.sub(old_pattern, new_html, content, count=1)

content = fix_image_container(4, "Mykorrhiza", "../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png", "['Mellan ekorren och fågeln sitter en varelse som inte liknar någonting.', 'Rötterna lyser.', 'Det är inte tydligt hur kopplingen mellan svampens hyfer (mycelet) och trädets rötter ser ut.']")
content = fix_image_container(5, "Havstulpaner på val", "../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png", "['Inga uppenbara felaktigheter?']")
content = fix_image_container(6, "Fästing på hund", "../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png", "['Fästingen har fem ben på sin högra sida.']")

# Fix Slide 7 Flashcard (Extract from content-grid)
s7_old = """                </div>
                <div class="flashcard-wrapper" style="margin-top: 0; align-self: stretch;">
                    <div class="flashcard" style="width: 100%;" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">konkurrens</div>
                        <div class="flashcard-back">När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser).</div>
                    </div>
                </div>
                </div>
            </div>"""
s7_new = """                </div>
            </div>
            
            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">konkurrens</div>
                        <div class="flashcard-back">När organismer tävlar om samma begränsade resurser i naturen (t.ex. mat, vatten eller boplatser).</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s7_old, s7_new)

# Fix Slide 8 Flashcard (Extract from content-grid)
s8_old = """                </div>
                <div class="flashcard-wrapper" style="margin-top: 0; align-self: stretch;">
                    <div class="flashcard" style="width: 100%;" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">ekologisk nisch</div>
                        <div class="flashcard-back">En arts "yrke" eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut.</div>
                    </div>
                </div>
                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>"""
s8_new = """                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>

            <div class="corner-flashcard">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">
                    <button class="expand-btn" onclick="openModal(event, this)" title="Visa i helskärm">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>
                        </svg>
                    </button>
                    <div class="flashcard-inner">
                        <div class="flashcard-front">ekologisk nisch</div>
                        <div class="flashcard-back">En arts "yrke" eller roll i ekosystemet (t.ex. vad den äter och hur den lever). Två arter kan inte ha exakt samma nisch på samma plats, för då konkurrerar de tills den ena slås ut.</div>
                    </div>
                </div>
            </div>"""
content = content.replace(s8_old, s8_new)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

