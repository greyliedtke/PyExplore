import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p


# making color a function of y...

x = np.linspace(0, 16, 50)
y = 6 * np.sin(x * .4)+8
pdata = bound_box(zip(x, y))
color_plot = []
for p in pdata:
    yv = p[1]/16
    xv = min(p[0]/16,1)
    print(xv)
    color = (xv, 1, 0)
    color_plot.append((p, color))

points = [
    ((8, 15), (1, 0, 0)),
    ((15, 8), (0, 1, 0)),
    ((8, 8), (0, .5, 1)),
    ((15, 15), (1, 1, 0))
]
fig, ax = plt.subplots()

for p in color_plot:
    ax.scatter(*p[0], c=[p[1]])

ax.set_xlim(0, 16)
ax.set_ylim(0, 16)
ax.set_aspect('equal')

st.pyplot(fig)