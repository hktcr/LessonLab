with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # The syntax error is around line 943: '        }\n' followed by '        function closeModal() {\n'
    # We can just check if the line is exactly '        }\n' and the next line is empty and the one after is closeModal
    if line == '        }\n' and i + 2 < len(lines) and 'function closeModal()' in lines[i+2]:
        pass # Skip this extra brace
    else:
        new_lines.append(line)

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.writelines(new_lines)
