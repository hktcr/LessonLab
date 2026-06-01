import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Update image tags to original images and add onclick
content = content.replace(
    '<img src="../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png" alt="Mykorrhiza">',
    '<img src="../assets/ekologi/mutualism_mykorrhiza_1777449230838.png" alt="Mykorrhiza" style="cursor: pointer;" onclick="openImageModal(this.src, \'../assets/ekologi/mutualism_mykorrhiza_notext_1777449752129_annotated.png\')">'
)

content = content.replace(
    '<img src="../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png" alt="Havstulpaner på val">',
    '<img src="../assets/ekologi/kommensalism_whale_1777449245313.png" alt="Havstulpaner på val" style="cursor: pointer;" onclick="openImageModal(this.src, \'../assets/ekologi/kommensalism_whale_notext_1777449769035_annotated.png\')">'
)

content = content.replace(
    '<img src="../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png" alt="Fästing på hund">',
    '<img src="../assets/ekologi/parasitism_tick_1777449259247.png" alt="Fästing på hund" style="cursor: pointer;" onclick="openImageModal(this.src, \'../assets/ekologi/parasitism_tick_notext_1777449783386_annotated.png\')">'
)

# 2. Add Image Modal HTML
image_modal_html = """
    <div id="imageModal" class="modal" onclick="if(event.target === this) closeImageModal()">
        <button class="modal-close" onclick="closeImageModal()">✕</button>
        <div class="modal-content" style="max-width: 90vw; display: flex; flex-direction: column; align-items: center;">
            <img id="modalImg" src="" style="max-width: 100%; max-height: 75vh; border-radius: 1.2rem; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6); object-fit: contain;">
            <div style="margin-top: 1.5rem;">
                <button id="toggleErrorBtn" class="fullscreen-btn" style="position: relative; right: auto; bottom: auto; margin: 0 auto; width: auto; padding: 0.8rem 1.5rem; font-family: inherit; font-size: 1.1rem; gap: 0.5rem; border-radius: 2rem;" onclick="toggleImageError()">
                    <span>🔍 Granska AI-felen (Hypotesmaskin)</span>
                </button>
            </div>
        </div>
    </div>
"""

content = content.replace('    <script>', image_modal_html + '\n    <script>')

# 3. Add Image Modal JS
image_modal_js = """
        let currentAnnotatedSrc = "";
        let currentOriginalSrc = "";
        let showingError = false;

        function openImageModal(originalSrc, annotatedSrc) {
            currentOriginalSrc = originalSrc;
            currentAnnotatedSrc = annotatedSrc;
            showingError = false;
            
            document.getElementById('modalImg').src = originalSrc;
            document.getElementById('imageModal').classList.add('active');
            
            const btn = document.getElementById('toggleErrorBtn');
            btn.innerHTML = '<span>🔍 Granska AI-felen (Hypotesmaskin)</span>';
            btn.style.color = 'var(--text)';
            btn.style.borderColor = 'rgba(255,255,255,0.2)';
            btn.style.background = 'rgba(255, 255, 255, 0.1)';
        }

        function closeImageModal() {
            document.getElementById('imageModal').classList.remove('active');
        }

        function toggleImageError() {
            showingError = !showingError;
            const img = document.getElementById('modalImg');
            const btn = document.getElementById('toggleErrorBtn');
            
            if (showingError) {
                img.src = currentAnnotatedSrc;
                btn.innerHTML = '<span>👁️ Dölj granskningsmarkeringar</span>';
                btn.style.color = 'var(--accent-neg)';
                btn.style.borderColor = 'var(--accent-neg)';
                btn.style.background = 'rgba(244, 63, 94, 0.1)';
            } else {
                img.src = currentOriginalSrc;
                btn.innerHTML = '<span>🔍 Granska AI-felen (Hypotesmaskin)</span>';
                btn.style.color = 'var(--text)';
                btn.style.borderColor = 'rgba(255,255,255,0.2)';
                btn.style.background = 'rgba(255, 255, 255, 0.1)';
            }
        }
"""

content = content.replace('        function closeModal() {', image_modal_js + '\n        function closeModal() {')

# 4. Modify Escape handler
content = content.replace('                closeModal();\n            }\n        });', '                closeModal();\n                closeImageModal();\n            }\n        });')

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

