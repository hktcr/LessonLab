with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'r') as f:
    content = f.read()

content = content.replace('mutualism_mykorrhiza_1777449230838.png', 'mutualism_mykorrhiza_notext_1777449752129_annotated.png')
content = content.replace('kommensalism_whale_1777449245313.png', 'kommensalism_whale_notext_1777449769035_annotated.png')
content = content.replace('parasitism_tick_1777449259247.png', 'parasitism_tick_notext_1777449783386_annotated.png')

with open('/Users/hakankarlsson/Library/CloudStorage/GoogleDrive-hlg.karlsson@gmail.com/Min enhet/🌎GAIA/GAIA-Repos/LessonLab/biologins-grunder/slides-ekologi.html', 'w') as f:
    f.write(content)
