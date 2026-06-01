import re

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

# Split slides
parts = content.split('<!-- Slide ')
header = parts[0]
slides = parts[1:]

def fix_image_slide(slide_html):
    # This slide has:
    # <div class="image-container">...</div>
    # <p class="subtitle"...>...</p>
    # <div class="glossary-grid"...>...</div>
    
    # We want to wrap the image-container and subtitle in a div, 
    # and the glossary-grid in another div, and put them both in a content-grid.
    
    # Extract parts
    img_match = re.search(r'<div class="image-container">[\s\S]*?</div>', slide_html)
    sub_match = re.search(r'<p class="subtitle" style="margin-top: 1.5rem; font-style: italic;">[\s\S]*?</p>', slide_html)
    grid_match = re.search(r'<div class="glossary-grid"[^>]*>[\s\S]*?</div>\n            </div>\n        </div>', slide_html)
    
    if img_match and sub_match and grid_match:
        img_str = img_match.group(0).replace('margin: 2rem auto;', 'margin: 0 auto;')
        sub_str = sub_match.group(0)
        
        # The grid match includes the closing tags of the slide because of the regex I used.
        # Let's extract just the glossary-grid
        gg_match = re.search(r'<div class="glossary-grid"[^>]*>[\s\S]*?(?=</div>\n        </div>)', slide_html)
        if not gg_match:
            return slide_html
            
        gg_str = gg_match.group(0)
        
        # Build new layout
        new_layout = f"""            <div class="content-grid" style="align-items: center; margin-top: 2rem;">
                <div>
{img_str}
{sub_str}
                </div>
                <div style="display: flex; justify-content: center;">
{gg_str.replace('margin-top: 3rem;', 'margin-top: 0; width: 100%; max-width: 400px;')}
                </div>
            </div>
        </div>"""
        
        # Replace the old parts
        slide_html = slide_html.replace(img_str, "")
        slide_html = slide_html.replace(sub_str, "")
        slide_html = slide_html.replace(gg_str + '\n        </div>', new_layout)
        
        # Clean up empty lines
        slide_html = re.sub(r'\n\s*\n\s*\n', '\n\n', slide_html)
        
    return slide_html

def fix_grid_slide(slide_html):
    # Move the flashcard from glossary-grid into the content-grid
    cg_match = re.search(r'<div class="content-grid"[^>]*>([\s\S]*?)</div>\n\s*<div class="glossary-grid"', slide_html)
    gg_match = re.search(r'<div class="glossary-grid"[^>]*>([\s\S]*?)(?=</div>\n        </div>)', slide_html)
    
    if cg_match and gg_match:
        cg_content = cg_match.group(1)
        # Extract just the flashcard (without the glossary-grid wrapper)
        fc_match = re.search(r'<div class="flashcard"[\s\S]*?</div>\n                </div>', gg_match.group(1))
        
        if fc_match:
            fc_html = fc_match.group(0)
            
            # The new content grid should have the flashcard as a 3rd item
            new_cg_content = cg_content + f"                <div style='display: flex; align-items: center; justify-content: center;'>\n    {fc_html}\n                </div>\n"
            
            # Replace old content-grid
            slide_html = slide_html.replace(cg_match.group(0), cg_match.group(0).replace(cg_content, new_cg_content))
            
            # Remove the old glossary-grid entirely
            slide_html = slide_html.replace(gg_match.group(0) + '</div>\n        </div>', '</div>')
            
    return slide_html


# Apply fixes
# Slide 3: Mutualism (index 3 because 0 is slide 1, 1 is slide 2...)
slides[3] = fix_image_slide(slides[3])
slides[4] = fix_image_slide(slides[4])
slides[5] = fix_image_slide(slides[5])

slides[6] = fix_grid_slide(slides[6])
slides[7] = fix_grid_slide(slides[7])

final_html = header + "".join(["<!-- Slide " + s for s in slides])

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(final_html)

