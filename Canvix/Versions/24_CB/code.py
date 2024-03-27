import colors

for c in dir(colors):
    if not c.startswith("__"):
        print(c)