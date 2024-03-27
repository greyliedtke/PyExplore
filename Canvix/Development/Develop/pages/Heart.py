import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p

# heart
with st.expander("Heart"):
    # Set the parameter t
    t = np.linspace(0, 2 * np.pi, 35)
    # Define the heart function using parametric equations
    scale = 0.35
    x = (16 * np.sin(t) ** 3) * scale
    y = (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)) * scale
    pdata = bound_box(zip(x, y))
    fig = plotter(pdata)
    st.pyplot(fig)

with st.expander("Sine Function"):
    y_factor = st.slider("Y Factor", min_value=1, max_value=10, value=7)
    x_factor = st.slider("X Factor", min_value=0.0, max_value=1.0, value=0.5)
    x = np.linspace(-8, 8, 100)
    y = y_factor * np.sin(x * x_factor)
    pdata = bound_box(zip(x, y))
    fig = plotter(pdata)
    st.pyplot(fig)

with st.expander("2 Sine"):
    x = np.linspace(-8, 8, 100)
    y = 3 * np.sin(x * 0.6) + 4
    x2 = np.linspace(-8, 8, 100)
    y2 = 3 * np.sin(x * 0.6) - 4
    w1 = bound_box(zip(x, y))
    w2 = bound_box(zip(x2, y2))
    fig = plotter(w1, w2)
    st.pyplot(fig)

with st.expander("Circle Function"):
    # y_factor = st.slider("Y Factor", min_value=1, max_value=10, value=7)
    # x_factor = st.slider("X Factor", min_value=0.0, max_value=1.0, value=.5)
    r = st.slider("Radius", min_value=1, max_value=10, value=6)
    xc, yc = 0, 0
    xr = np.linspace(-np.pi, np.pi, 100)
    x = xc + r * np.cos(xr)
    y = yc + r * np.sin(xr)
    pdata = bound_box(zip(x, y))
    fig = plotter(pdata)
    st.pyplot(fig)

<<<<<<< HEAD
with st.expander("Time Circle"):
    h = 8
    m = 32
    s = 44
    hf, mf, sf = h / 12, m / 60, s / 60

    tdc = (8, 15)
    rdc = (15, 8)
    p1 = [8, 8]
    p2 = [15, 15]
    l12 = p_to_p(p1, p2)
    xr = np.linspace(p1[0], p1[0] + l12[2], 50)
    y = l12[0] * (xr - p1[0]) + l12[1] + p1[1]
    pdata = bound_box(zip(xr, y))
    fig = plotter(pdata, matrix=True)
    st.pyplot(fig)
=======



>>>>>>> 2d3377a12b6b5a789556bd540adf9b6ff110c9b1
