import re

file_path = "/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_module = """        // ══════════════════════════════════════
        // WINDING PATH (Slingrande Väg)
        // ══════════════════════════════════════
        const WHEEL = (() => {
            const CX = 350;
            const NODE_GAP_Y = 140;
            const AMPLITUDE = 160;
            
            const COLORS = {
                kemi:    { solid: '#f59e0b', light: 'rgba(245,158,11,0.2)' },
                fysik:   { solid: '#3b82f6', light: 'rgba(59,130,246,0.2)' },
                biologi: { solid: '#10b981', light: 'rgba(16,185,129,0.2)' },
                kroppen: { solid: '#f43f5e', light: 'rgba(244,63,94,0.2)' }
            };

            function render(year) {
                const svg = document.getElementById('wheelSvg');
                const legend = document.getElementById('wheelLegend');
                const nodes = yearData[year];
                
                // Update UI text
                const labelEl = document.getElementById('wheelYearLabel');
                if(labelEl) labelEl.textContent = `Årskurs ${year}`;
                const titleNode = document.querySelector('.wheel-modal-title');
                if(titleNode) titleNode.innerHTML = titleNode.innerHTML.replace('Årshjul', 'Slingrande Väg');
                const btnSpan = document.querySelector('.wheel-btn span');
                if(btnSpan) btnSpan.textContent = 'Översikt';

                document.querySelectorAll('.wm-tab').forEach(t => {
                    t.classList.toggle('active', parseInt(t.dataset.year) === year);
                });

                const totalHeight = Math.max(600, nodes.length * NODE_GAP_Y + 160);
                svg.setAttribute('viewBox', `0 0 700 ${totalHeight}`);
                
                let svgContent = '';
                
                let d = '';
                const points = [];
                nodes.forEach((node, i) => {
                    const isRight = i % 2 === 0;
                    const x = CX + (isRight ? AMPLITUDE : -AMPLITUDE);
                    const y = 80 + i * NODE_GAP_Y;
                    points.push({x, y});
                });
                
                if (points.length > 0) {
                    d += `M ${CX},20 `;
                    d += `C ${CX},${points[0].y/2} ${points[0].x},${points[0].y/2} ${points[0].x},${points[0].y} `;
                    for (let i = 0; i < points.length - 1; i++) {
                        const p1 = points[i];
                        const p2 = points[i+1];
                        const midY = (p1.y + p2.y) / 2;
                        d += `C ${p1.x},${midY} ${p2.x},${midY} ${p2.x},${p2.y} `;
                    }
                    d += `C ${points[points.length-1].x},${totalHeight-40} ${CX},${totalHeight-40} ${CX},${totalHeight-10}`;
                    
                    svgContent += `<path d="${d}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="12" stroke-linecap="round" />`;
                    svgContent += `<path d="${d}" fill="none" stroke="var(--accent-blue)" stroke-width="2" stroke-linecap="round" stroke-dasharray="8 8" opacity="0.6" style="animation: dash 30s linear infinite;"/>`;
                }

                nodes.forEach((node, i) => {
                    const p = points[i];
                    const c = COLORS[node.subject] || COLORS.kemi;
                    const hasContent = node.lessons.length > 0;
                    const opacity = hasContent ? '1' : '0.4';
                    
                    svgContent += `<circle cx="${p.x}" cy="${p.y}" r="35" fill="${c.light}" opacity="${opacity}" class="wheel-arc" data-id="${node.id}" style="cursor:pointer; transition: all 0.3s;" />`;
                    svgContent += `<circle cx="${p.x}" cy="${p.y}" r="25" fill="rgba(10,14,23,1)" stroke="${c.solid}" stroke-width="3" opacity="${opacity}" style="pointer-events:none"/>`;
                    
                    const abbr = {kemi:'Ke',fysik:'Fy',biologi:'Bi',kroppen:'Kr'}[node.subject] || '';
                    svgContent += `<text x="${p.x}" y="${p.y}" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="700" fill="white" opacity="${opacity}" font-family="Inter,sans-serif" style="pointer-events:none">${abbr}</text>`;
                    
                    const isRight = i % 2 === 0;
                    const labelX = isRight ? p.x - 50 : p.x + 50;
                    const anchor = isRight ? 'end' : 'start';
                    
                    svgContent += `<line x1="${p.x + (isRight?-30:30)}" y1="${p.y}" x2="${labelX + (isRight?10:-10)}" y2="${p.y}" stroke="${c.solid}" stroke-width="1" opacity="0.4" />`;
                    
                    svgContent += `<text x="${labelX}" y="${p.y - 8}" text-anchor="${anchor}" dominant-baseline="central" fill="${c.solid}" font-size="16" font-weight="700" font-family="Inter,sans-serif" class="wheel-label" data-id="${node.id}" style="cursor:pointer">${node.title}</text>`;
                    svgContent += `<text x="${labelX}" y="${p.y + 12}" text-anchor="${anchor}" dominant-baseline="central" fill="rgba(255,255,255,0.4)" font-size="12" font-family="Inter,sans-serif" style="pointer-events:none">${node.season} · ${node.weeks} v · ${hasContent ? node.lessons.length + ' manus' : 'planerat'}</text>`;
                });
                
                svg.innerHTML = svgContent;

                svg.querySelectorAll('.wheel-arc, .wheel-label').forEach(el => {
                    el.addEventListener('click', (e) => {
                        const id = e.target.dataset.id;
                        if (id) {
                            closeWheel();
                            setYear(year);
                            setTimeout(() => {
                                expandedCardId = id;
                                toggleCard(id);
                                const card = document.querySelector(` + "`[data-card-id=\"${id}\"]`" + `);
                                if (card) card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            }, 350);
                        }
                    });
                    el.addEventListener('mouseenter', () => {
                        const id = el.dataset.id;
                        svg.querySelectorAll(` + "`circle[data-id=\"${id}\"]`" + `).forEach(s => {
                            if(s.getAttribute('r') === '35') s.setAttribute('r', '45');
                        });
                    });
                    el.addEventListener('mouseleave', () => {
                        const id = el.dataset.id;
                        svg.querySelectorAll(` + "`circle[data-id=\"${id}\"]`" + `).forEach(s => {
                            if(s.getAttribute('r') === '45') s.setAttribute('r', '35');
                        });
                    });
                });

                const subjects = [...new Set(nodes.map(n => n.subject))];
                legend.innerHTML = subjects.map(s => {
                    const c = COLORS[s] || COLORS.kemi;
                    const name = { kemi: 'Kemi', fysik: 'Fysik', biologi: 'Biologi', kroppen: 'Kroppen' }[s] || s;
                    return ` + "`<span class=\"wheel-legend-item\"><span class=\"wheel-legend-dot\" style=\"background:${c.solid}\"></span>${name}</span>`" + `;
                }).join('');
            }

            return { render };
        })();"""

pattern = re.compile(r"// ══════════════════════════════════════\n\s*// YEAR WHEEL\n\s*// ══════════════════════════════════════(.*?)return { render };\n\s*}\)\(\);", re.DOTALL)
new_content = pattern.sub(new_module, content)

# Let's also add CSS for dash animation if missing
if "@keyframes dash" not in new_content:
    css_injection = """
    <style>
        @keyframes dash {
            to { stroke-dashoffset: -1000; }
        }
        .wheel-modal-body {
            overflow-y: auto;
            max-height: 70vh;
        }
    </style>
</head>"""
    new_content = new_content.replace("</head>", css_injection)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Path replaced!")
