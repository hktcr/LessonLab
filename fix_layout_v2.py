with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# Fix Slide 4
s4_old = """            <div class="image-container">
                <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png')">
            </div>
            <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
            </p>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s4_new = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: mykorrhiza (träd och svamp) eller lavar (svamp och alg)
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""
content = content.replace(s4_old, s4_new)

# Slide 4 closing
s4_old_end = """                </div>
            </div>
        </div><!-- Slide 5"""
s4_new_end = """                </div>
            </div>
            </div>
        </div><!-- Slide 5"""
content = content.replace(s4_old_end, s4_new_end)

# Fix Slide 5
s5_old = """            <div class="image-container">
                <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png')">
            </div>
            <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                Exempel: havstulpaner som får biologisk snålskjuts av valar.
            </p>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s5_new = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: havstulpaner som får biologisk snålskjuts av valar.
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""
content = content.replace(s5_old, s5_new)

# Slide 5 closing
s5_old_end = """                </div>
            </div>
        </div><!-- Slide 6"""
s5_new_end = """                </div>
            </div>
            </div>
        </div><!-- Slide 6"""
content = content.replace(s5_old_end, s5_new_end)

# Fix Slide 6
s6_old = """            <div class="image-container">
                <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png')">
            </div>
            <p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">
                Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
            </p>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s6_new = """            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
                    <div class="image-container" style="margin: 0 auto;">
                        <img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund" style="max-height: 40vh; cursor: pointer;" onclick="openImageModal(this.src, '../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png')">
                    </div>
                    <p class="subtitle" style="margin-top: 1rem; font-style: italic;">
                        Exempel: fästingar suger blod för att utvinna energi från värdorganismen.
                    </p>
                </div>
                <div class="glossary-grid" style="margin-top: 0; width: 100%; max-width: 400px; justify-self: center;">"""
content = content.replace(s6_old, s6_new)

# Slide 6 closing
s6_old_end = """                </div>
            </div>
        </div><!-- Slide 7"""
s6_new_end = """                </div>
            </div>
            </div>
        </div><!-- Slide 7"""
content = content.replace(s6_old_end, s6_new_end)

# Fix Slide 7
s7_old = """                    </ul>
                </div>
            </div>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s7_new = """                    </ul>
                </div>
                <div style="display: flex; align-items: center; justify-content: center; width: 100%;">"""
content = content.replace(s7_old, s7_new)

s7_old_end = """                    </div>
                </div>
            </div>
        </div><!-- Slide 8"""
s7_new_end = """                    </div>
                </div>
                </div>
            </div>
        </div><!-- Slide 8"""
content = content.replace(s7_old_end, s7_new_end)

# Fix Slide 8
s8_old = """            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s8_new = """            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>
        </div><!-- end slide content -->
        """
        
# Actually for Slide 8, the flashcard can also go into content-grid
s8_full_old = """                    </ul>
                </div>
            </div>

            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>
        
            <div class="glossary-grid" style="margin-top: 3rem;">"""
s8_full_new = """                    </ul>
                </div>
                <div style="display: flex; align-items: center; justify-content: center; width: 100%;">"""
content = content.replace(s8_full_old, s8_full_new)

# And move the subtitle to the end
s8_end_old = """                    </div>
                </div>
            </div>
        </div><!-- Slide 9"""
s8_end_new = """                    </div>
                </div>
                </div>
            </div>
            <p class="subtitle" style="margin-top: 2rem;">
                Resultat: de lever i samma skog, men har delat upp resurserna.
            </p>
        </div><!-- Slide 9"""
content = content.replace(s8_end_old, s8_end_new)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)
