"""
control page to serve as command center for engine
streamlit run ScaledWiki/SubTesting/SControl/Control.py
"""

from nicegui import ui
import random

# handling correct answer...
cor = "E5"

# ------------------------------------------------------
# chess board
cols = [1, 2, 3, 4, 5, 6, 7, 8]
rows = [1, 2, 3, 4, 5, 6, 7, 8]

ck = ["A", "B", "C", "D", "E", "F", "G", "H"]

mat = []

def b_clicker(inp):
    if inp == cor:
        print("f yeah")
        newc = f"{ck[random.randint(1,8)-1]}{random.randint(1,8)}"
        print(newc)
    else:
        print("x")


def create_b(c, r):
    grid = f"{ck[c-1]}{r}"
    ui.button("xx", on_click=lambda:b_clicker(f"{ck[c-1]}{r}"))

for c in cols:
    with ui.row():
        for r in rows:
            create_b(c,r)

# running the page
ui.run(title="PiMan", port=2999, binding_refresh_interval=0.5)

# ------------------------------------------------------
