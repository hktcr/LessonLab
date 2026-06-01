import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# 1. Add Text Zoom Buttons
new_buttons = """        <div style="position: fixed; bottom: 2rem; right: 2.5rem; display: flex; gap: 1rem; z-index: 100;">
            <div style="display: flex; background: rgba(0,0,0,0.2); border-radius: 0.5rem; border: 1px solid rgba(255,255,255,0.1); overflow: hidden;">
                <button class="action-btn" style="border-radius: 0; border: none; width: 40px;" onclick="zoomText('out')" title="Minska text">A-</button>
                <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
                <button class="action-btn" style="border-radius: 0; border: none; width: 40px;" onclick="zoomText('in')" title="Öka text">A+</button>
            </div>
            <button class="action-btn" onclick="openOverviewModal()" title="Översikt (Alla slides)">
"""

content = content.replace('        <div style="position: fixed; bottom: 2rem; right: 2.5rem; display: flex; gap: 1rem; z-index: 100;">\n            <button class="action-btn" onclick="openOverviewModal()" title="Översikt (Alla slides)">', new_buttons)

# 2. Add Zoom JavaScript
zoom_js = """
        // Zoom functionality
        let currentZoom = 100;
        function zoomText(direction) {
            if(direction === 'in' && currentZoom < 180) currentZoom += 10;
            else if(direction === 'out' && currentZoom > 50) currentZoom -= 10;
            document.documentElement.style.fontSize = currentZoom + '%';
        }
"""
content = content.replace('        // Fullscreen functionality', zoom_js + '\n        // Fullscreen functionality')

# 3. Fix the "Granska" modal image logic to use a CSS overlay instead of changing the image source!
overlay_html = """
        <div class="modal-content" style="max-width: 90vw; display: flex; flex-direction: column; align-items: center; position: relative;">
            <div style="position: relative; display: inline-block;">
                <img id="modalImg" src="" style="max-width: 100%; max-height: 75vh; border-radius: 1.2rem; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6); object-fit: contain;">
                
                <div id="aiErrorOverlay" style="display: none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; border: 8px solid var(--accent-neg); border-radius: 1.2rem; pointer-events: none;">
                    <div style="position: absolute; top: 1rem; left: 1rem; background: var(--accent-neg); color: white; padding: 1rem 2rem; border-radius: 0.5rem; font-weight: bold; font-size: 1.5rem; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
                        ⚠️ AI-hallucinationer upptäckta!
                        <ul style="font-size: 1.1rem; font-weight: normal; margin-top: 0.5rem; padding-left: 1.5rem;">
                            <li>Felstavade påhittade ord</li>
                            <li>Biologiska fel (t.ex. fel antal ben)</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div style="margin-top: 1.5rem;">
"""
content = content.replace('        <div class="modal-content" style="max-width: 90vw; display: flex; flex-direction: column; align-items: center;">\n            <img id="modalImg" src="" style="max-width: 100%; max-height: 75vh; border-radius: 1.2rem; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6); object-fit: contain;">\n            <div style="margin-top: 1.5rem;">', overlay_html)

# 4. Update the toggleImageError JS
new_toggle_js = """
        function toggleImageError() {
            showingError = !showingError;
            const btn = document.getElementById('toggleErrorBtn');
            const overlay = document.getElementById('aiErrorOverlay');
            
            if (showingError) {
                overlay.style.display = 'block';
                btn.innerHTML = '<span>👁️ Dölj granskningsmarkeringar</span>';
                btn.style.color = 'var(--accent-neg)';
                btn.style.borderColor = 'var(--accent-neg)';
                btn.style.background = 'rgba(244, 63, 94, 0.1)';
            } else {
                overlay.style.display = 'none';
                btn.innerHTML = '<span>🔍 Granska AI-felen (Hypotesmaskin)</span>';
                btn.style.color = 'var(--text)';
                btn.style.borderColor = 'rgba(255,255,255,0.2)';
                btn.style.background = 'rgba(255, 255, 255, 0.1)';
            }
        }
"""
# Need to replace the old toggleImageError block safely
content = re.sub(r'        function toggleImageError\(\) \{[\s\S]*?\}\n', new_toggle_js, content)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)

