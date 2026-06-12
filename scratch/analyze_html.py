import os
import glob

html_files = glob.glob('**/*.html', recursive=True)
generated = [f for f in html_files if os.path.basename(f).startswith('lektion-')]

print(f"Found {len(generated)} generated lesson files.")
css_errors = 0
markdown_errors = 0
for g in generated:
    with open(g, 'r') as f:
        content = f.read()
        if 'styles.css' in content or 'href="style.css"' in content: # missing ../
            css_errors += 1
        if '**' in content:
            markdown_errors += 1

print(f"CSS link broken in {css_errors} files.")
print(f"Markdown bolding broken in {markdown_errors} files.")
