import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Add CSS
css_to_add = """
        .slide-split {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
            align-items: center;
            width: 100%;
            max-width: 1300px;
            margin-top: 1rem;
        }
        .slide-split > div {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .flashcard-wrapper {
            display: flex;
            justify-content: center;
            width: 100%;
        }
"""
content = content.replace("</style>", css_to_add + "</style>")

# 2. Update openImageModal function
old_modal_js = """        function openImageModal(originalSrc, annotatedSrc) {
            currentOriginalSrc = originalSrc;
            currentAnnotatedSrc = annotatedSrc;
            showingError = false;
            
            document.getElementById('modalImg').src = originalSrc;
            document.getElementById('imageModal').classList.add('active');
            
            const btn = document.getElementById('toggleErrorBtn');"""

new_modal_js = """        function openImageModal(originalSrc, annotatedSrc, errorTexts) {
            currentOriginalSrc = originalSrc;
            currentAnnotatedSrc = annotatedSrc;
            showingError = false;
            
            document.getElementById('modalImg').src = originalSrc;
            
            const overlay = document.getElementById('aiErrorOverlay');
            let listHtml = "";
            if (errorTexts && errorTexts.length > 0) {
                listHtml = '<ul style="font-size: 1.1rem; font-weight: normal; margin-top: 0.5rem; padding-left: 1.5rem;">';
                errorTexts.forEach(t => {
                    listHtml += `<li>${t}</li>`;
                });
                listHtml += '</ul>';
            } else {
                listHtml = '<ul style="font-size: 1.1rem; font-weight: normal; margin-top: 0.5rem; padding-left: 1.5rem;"><li>Biologiska fel</li></ul>';
            }
            
            overlay.innerHTML = `
                <div style="position: absolute; top: 1rem; left: 1rem; background: var(--accent-neg); color: white; padding: 1rem 2rem; border-radius: 0.5rem; font-weight: bold; font-size: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.5); max-width: 80%; text-align: left;">
                    ⚠️ AI-hallucinationer upptäckta!
                    ${listHtml}
                </div>
            `;
            
            document.getElementById('imageModal').classList.add('active');
            
            const btn = document.getElementById('toggleErrorBtn');"""

content = content.replace(old_modal_js, new_modal_js)

# 3. Update Slide 4 (Mutualism)
s4_old = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""

s4_new = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Rötterna lyser konstlat som neonkablar i jorden', 'Svampar växer direkt ur tjocka rötter istället för att hyferna kopplar till rotspetsarna', 'Trädstammen har obegriplig AI-text/mönster inristat'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">"""
content = content.replace(s4_old, s4_new)

# Slide 4 closing fix
content = content.replace("""                    </div>
                </div>
            </div>
            </div>
        </div><!-- Slide 5""", """                    </div>
                </div>
            </div>
        </div><!-- Slide 5""")

# 4. Update Slide 5 (Kommensalism)
s5_old = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: havstulpaner som får biologisk snålskjuts av valar.
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""
s5_new = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Havstulpanerna ser ut som faktiska blommor/tulpaner istället för kräftdjur med kalkskal', 'De växer i ett för perfekt, symmetriskt mönster på valen'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: havstulpaner som får biologisk snålskjuts av valar.
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">"""
content = content.replace(s5_old, s5_new)

# Slide 5 closing fix
content = content.replace("""                    </div>
                </div>
            </div>
            </div>
        </div><!-- Slide 6""", """                    </div>
                </div>
            </div>
        </div><!-- Slide 6""")

# 5. Update Slide 6 (Parasitism)
s6_old = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""
s6_new = """            <div class="slide-split">
                <div>
                    <div class="image-container" style="margin: 0 auto; width: 100%;">
                        <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="max-height: 48vh; cursor: pointer; width: 100%; object-fit: cover;" onclick="openImageModal(this.src, this.src, ['Fästingen verkar ha fel antal ben eller felaktiga proportioner för ett spindeldjur', 'Kroppen är helt massiv och proportionerna mot hårstråna är ofta helt orimliga i AI-bilder'])">
                    </div>
                    <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                        Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
                    </p>
                </div>
                <div class="flashcard-wrapper">
                    <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 450px;">"""
content = content.replace(s6_old, s6_new)

# Slide 6 closing fix
content = content.replace("""                    </div>
                </div>
            </div>
            </div>
        </div><!-- Slide 7""", """                    </div>
                </div>
            </div>
        </div><!-- Slide 7""")

# Slide 7 fixing content-grid to 3 columns explicitly so flashcard fits nicely
content = content.replace("""            <div class="content-grid" style="margin-top: 3rem;">""", """            <div class="content-grid" style="margin-top: 2rem; grid-template-columns: repeat(3, 1fr); align-items: start;">""")

# Slide 8 fixing content-grid to 3 columns
content = content.replace("""            <div class="content-grid" style="margin: 3rem 0;">""", """            <div class="content-grid" style="margin: 3rem 0; grid-template-columns: repeat(3, 1fr); align-items: start;">""")

# One more closing tag fix that I introduced with fix_layout_v2:
content = content.replace("""                <div style="display: flex; align-items: center; justify-content: center; width: 100%;">
                <div class="flashcard" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">""", """                <div class="flashcard-wrapper" style="margin-top: 0; align-self: stretch;">
                    <div class="flashcard" style="width: 100%;" onclick="if(!event.target.closest('.expand-btn')) this.classList.toggle('flipped')">""")

content = content.replace("""                </div>
                </div>
            </div>
        </div><!-- Slide 8""", """                </div>
                </div>
            </div>
        </div><!-- Slide 8""")

content = content.replace("""                </div>
                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">""", """                </div>
                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">""")


# Also need to remove the static aiErrorOverlay block because we inject it dynamically now
# Actually we inject innerHTML into overlay, so it's fine. 

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

