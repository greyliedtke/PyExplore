import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p, perim
from Tools.Matrix import char_matrix

# making color a function of y...
c_r = st.number_input("Red", value=1, max_value=9, min_value=0)
c_g = st.number_input("Green", value=1, max_value=9, min_value=0)
c_b = st.number_input("Blue", value=1, max_value=9, min_value=0)


p_r = char_matrix('r', [2,11])
p_g = char_matrix('g', [12,11])
p_b = char_matrix('b', [8,2])

x= range(16)
y_r = range(16)
bd = []
for i in x:
    for j in y_r:
        bd.append([i, j])

bd = perim(8,8)

color_plot = []
for p in bd:
    yv = p[1]/16
    xv = min(p[0]/16,1)
    color = (xv, 1, 0)
    color_plot.append((p, [c_r/9, c_g/9, c_b/9]))

for r in p_r:
    color_plot.append((r, [1, 0, 0]))
for r in p_g:
    color_plot.append((r, [0, 1, 0]))
for r in p_b:
    color_plot.append((r, [0, 0, 1]))

fig, ax = plt.subplots()

for p in color_plot:
    ax.scatter(*p[0], c=[p[1]])

ax.set_xlim(0, 16)
ax.set_ylim(0, 16)
ax.set_aspect('equal')

st.pyplot(fig)