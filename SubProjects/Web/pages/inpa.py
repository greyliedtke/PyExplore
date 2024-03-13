import streamlit as st

import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()
l = .9

def draw_seg(origin, angle):
    angle = math.radians(angle)
    px0 = -l*math.cos(angle) 
    py0 = -l*math.sin(angle) 
    px1 = l*math.cos(angle)
    py1 = l*math.sin(angle)
    xs = [origin[0]+x for x in [px0,0, px1]]
    ys = [origin[1]+y for y in [py0,0, py1]]
    return xs, ys

sos = [
    [1,4],
    [3,4],
    [1,2],
    [3,2],
    [2,5],
    [2,3],
    [2,1]
]


def create_seg(seg_a):
    sa = []
    for i,s in enumerate(seg_a):
        sa.append(draw_seg(sos[i], s))
    return sa

s1 = st.selectbox("Angle 1", [0,30,60,90])
s2 = st.number_input("Angle 2", 0, 360, 0)
s3 = st.number_input("Angle 3", 0, 360, 0)
s4 = st.number_input("Angle 4", 0, 360, 0)
s5 = st.number_input("Angle 5", 0, 360, 0)
s6 = st.number_input("Angle 6", 0, 360, 0)
s7 = st.number_input("Angle 7", 0, 360, 0)


sas = [s1, s2, s3, s4, s5, s6, s7]

for i,s in enumerate(sas):
    xp = draw_seg(sos[i], s)
    xs = [x+3*(i) for x in xp[0]]
    ax.plot(xp[0], xp[1], color="black")

ax.set_xlim(0, 18)
ax.set_ylim(0, 18)
st.pyplot(fig)
