import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p


# making color a function of y...
xs = -.45
yh = 13
x = np.linspace(0, 16, 50)
y = xs*(x-9)**2 + yh
yr = xs*(x-11)**2 + yh
pl = bound_box(zip(x, y))
pr = bound_box(zip(x, yr))
color_plot = []
for p in pl:
    yv = min(max(0,p[1])/16,1)
    xv = min(max(0,p[0])/16,1)
    color = (1, 0, yv)
    color_plot.append((p, color))
for p in pr:
    yv = min(max(0,p[1])/16,1)
    xv = min(max(0,p[0])/16,1)
    color = (0, 1, yv)
    color_plot.append((p, color))

fig, ax = plt.subplots()

for p in color_plot:
    ax.scatter(*p[0], c=[p[1]])

ax.set_xlim(0, 16)
ax.set_ylim(0, 16)
ax.set_aspect('equal')

st.pyplot(fig)