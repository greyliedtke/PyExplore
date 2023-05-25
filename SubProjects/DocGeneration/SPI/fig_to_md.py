# get all files

import glob
directory = 'ScaledWiki/Tests/Task07/1_24_23/Figs'
pngs = glob.glob(directory + '/*')


import markdown


output = ""

for figure in pngs:
    output += "![](%s)\n" % figure

with open("Figures.md", "w") as f:
    f.write(markdown.markdown(output))


