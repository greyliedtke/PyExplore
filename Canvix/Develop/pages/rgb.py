import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p


# making color a function of y...
c_r = st.number_input("Red", value=1, max_value=9, min_value=0)
c_g = st.number_input("Green", value=1, max_value=9, min_value=0)
c_b = st.number_input("Blue", value=1, max_value=9, min_value=0)

x = np.linspace(0, 16, 50)
y = 6 * np.sin(x * .4)+8
pdata = bound_box(zip(x, y))
color_plot = []
for p in pdata:
    yv = p[1]/16
    xv = min(p[0]/16,1)
    print(xv)
    color = (xv, 1, 0)
    color_plot.append((p, [c_r/9, c_g/9, c_b/9]))

fig, ax = plt.subplots()

for p in color_plot:
    ax.scatter(*p[0], c=[p[1]])

ax.set_xlim(0, 16)
ax.set_ylim(0, 16)
ax.set_aspect('equal')

st.pyplot(fig)