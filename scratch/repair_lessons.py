import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
generated = [f for f in html_files if os.path.basename(f).startswith('lektion-')]

fixed_count = 0

for filepath in generated:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # 1. Fix CSS link
    content = content.replace('href="../styles.css"', 'href="../style.css"')
    content = content.replace('href="styles.css"', 'href="style.css"')
    
    # 2. Fix Markdown bolding
    # **text** -> <strong>text</strong>
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    
    # 3. Clean up list artifacts in paragraphs
    # <p>*   <strong> -> <p>• <strong>
    # <p>* <strong> -> <p>• <strong>
    content = re.sub(r'<p>\s*\*\s*', '<p>• ', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1

print(f"Repaired {fixed_count} lesson files successfully.")
