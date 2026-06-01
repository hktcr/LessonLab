import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Remove the global zoom buttons
global_zoom_html = """            <div style="display: flex; background: rgba(0,0,0,0.2); border-radius: 0.5rem; border: 1px solid rgba(255,255,255,0.1); overflow: hidden;">
                <button class="action-btn" style="border-radius: 0; border: none; width: 40px;" onclick="zoomText('out')" title="Minska text">A-</button>
                <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
                <button class="action-btn" style="border-radius: 0; border: none; width: 40px;" onclick="zoomText('in')" title="Öka text">A+</button>
            </div>\n"""
content = content.replace(global_zoom_html, "")

# 2. Modify flashcardModal
old_modal = """    <div id="flashcardModal" class="modal" onclick="if(event.target === this) closeModal()">
        <button class="modal-close" onclick="closeModal()">✕</button>
        <div class="modal-content">
            <h2 id="modalWord" style="color: var(--accent-neu); font-size: clamp(3rem, 6vw, 5rem); margin-bottom: 2rem; text-transform: capitalize;"></h2>
            <p id="modalExplanation" style="font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.6; color: var(--text);"></p>
        </div>
    </div>"""

new_modal = """    <div id="flashcardModal" class="modal" onclick="if(event.target === this) closeModal()">
        <button class="modal-close" onclick="closeModal()">✕</button>
        <div class="modal-content" style="position: relative; padding-bottom: 5rem; min-width: 60vw;">
            <h2 id="modalWord" style="color: var(--accent-neu); font-size: 4rem; margin-bottom: 2rem; text-transform: capitalize; transition: font-size 0.2s;"></h2>
            <p id="modalExplanation" style="font-size: 2.2rem; line-height: 1.6; color: var(--text); transition: font-size 0.2s;"></p>
            
            <div style="position: absolute; bottom: 0; right: 0; display: flex; background: rgba(0,0,0,0.4); border-radius: 0.5rem; border: 1px solid rgba(255,255,255,0.2); overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.5);">
                <button class="action-btn" style="border-radius: 0; border: none; width: 50px; height: 50px; font-size: 1.2rem; font-weight: bold; background: transparent;" onclick="zoomModalText('out')" title="Minska text">A-</button>
                <div style="width: 1px; background: rgba(255,255,255,0.2);"></div>
                <button class="action-btn" style="border-radius: 0; border: none; width: 50px; height: 50px; font-size: 1.4rem; font-weight: bold; background: transparent;" onclick="zoomModalText('in')" title="Öka text">A+</button>
            </div>
        </div>
    </div>"""

content = content.replace(old_modal, new_modal)

# 3. Update openModal to reset zoom
old_open_modal = """        function openModal(event, btn) {
            event.stopPropagation();
            const cardInner = btn.nextElementSibling;
            const word = cardInner.querySelector('.flashcard-front').textContent;
            const explanation = cardInner.querySelector('.flashcard-back').textContent;
            
            document.getElementById('modalWord').textContent = word;
            document.getElementById('modalExplanation').textContent = explanation;
            document.getElementById('flashcardModal').classList.add('active');
        }"""

new_open_modal = """        let modalZoom = 1.0;
        function zoomModalText(direction) {
            if(direction === 'in' && modalZoom < 2.0) modalZoom += 0.2;
            else if(direction === 'out' && modalZoom > 0.5) modalZoom -= 0.2;
            
            document.getElementById('modalWord').style.fontSize = (4 * modalZoom) + 'rem';
            document.getElementById('modalExplanation').style.fontSize = (2.2 * modalZoom) + 'rem';
        }

        function openModal(event, btn) {
            event.stopPropagation();
            
            // Reset zoom
            modalZoom = 1.0;
            document.getElementById('modalWord').style.fontSize = '4rem';
            document.getElementById('modalExplanation').style.fontSize = '2.2rem';
            
            const cardInner = btn.nextElementSibling;
            const word = cardInner.querySelector('.flashcard-front').textContent;
            const explanation = cardInner.querySelector('.flashcard-back').textContent;
            
            document.getElementById('modalWord').textContent = word;
            document.getElementById('modalExplanation').textContent = explanation;
            document.getElementById('flashcardModal').classList.add('active');
        }"""

content = content.replace(old_open_modal, new_open_modal)

# 4. Remove old zoomText function
old_zoom_text = """        // Zoom functionality
        let currentZoom = 100;
        function zoomText(direction) {
            if(direction === 'in' && currentZoom < 180) currentZoom += 10;
            else if(direction === 'out' && currentZoom > 50) currentZoom -= 10;
            document.documentElement.style.fontSize = currentZoom + '%';
        }"""
content = content.replace(old_zoom_text, "")

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

