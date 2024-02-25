import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import math
from Tools.Plot import bound_box, plotter, p_to_p

# heart
with st.expander("Heart"):
    # Set the parameter t
    t = np.linspace(0, 2*np.pi, 50)
    # Define the heart function using parametric equations
    scale = .4
    x = (16*np.sin(t)**3)*scale
    y = (13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t))*scale
    pdata = bound_box(zip(x,y))
    fig = plotter(pdata)
    st.pyplot(fig)

with st.expander("Sine Function"):
    y_factor = st.slider("Y Factor", min_value=1, max_value=10, value=7)
    x_factor = st.slider("X Factor", min_value=0.0, max_value=1.0, value=.5)
    x = np.linspace(-8, 8, 100)
    y = y_factor*np.sin(x*x_factor)
    pdata = bound_box(zip(x,y))
    fig = plotter(pdata)
    st.pyplot(fig)

with st.expander("Circle Function"):
    # y_factor = st.slider("Y Factor", min_value=1, max_value=10, value=7)
    # x_factor = st.slider("X Factor", min_value=0.0, max_value=1.0, value=.5)
    r = st.slider("Radius", min_value=1, max_value=10, value=6)
    xc,yc = 0,0
    xr = np.linspace(-np.pi, np.pi, 100)
    x = xc + r * np.cos(xr)
    y = yc + r * np.sin(xr)
    pdata = bound_box(zip(x,y))
    fig = plotter(pdata)
    st.pyplot(fig)




