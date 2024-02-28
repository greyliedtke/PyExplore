from Tools.Plot import bound_box, plotter, p_to_p
import streamlit as st
import math
import numpy as np


def deg_to_slope(rad):
    # Compute the slope using trigonometric functions
    rad = -rad+math.pi/2
    slope = math.tan(rad)
    return slope

tin = st.text_input("Enter a number", "12:34")
h = st.number_input("Hour", value=3)
m = st.number_input("Minute", value=40)
hf, mf = h/12, m/60
hx = deg_to_slope(hf*2*math.pi)
mx = deg_to_slope(mf*2*math.pi)

m_point = mx*8, 

tdc = (8, 15)
rdc = (15, 8)
p1 = [8,8]
p2 = [15,15]
l12 = p_to_p(p1, p2)
xr = np.linspace(p1[0], p1[0]+l12[2], 50)
y = l12[0]*(xr-p1[0]) + p1[1]
pdata = bound_box(zip(xr,y))
fig = plotter(pdata, matrix=True)
st.pyplot(fig)

