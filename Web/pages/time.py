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

off = 135
von = 90
hon = 0

def create_seg(seg_a):
    sa = []
    for i,s in enumerate(seg_a):
        sa.append(draw_seg(sos[i], s))
    return sa

zero = create_seg([off, off, off, off, off, off, off])
# zero = create_seg([von, von, von, von, hon, off, hon])
one = create_seg([off, von, off, von, off, off, off])
two = create_seg([off, von, von, off, hon, hon, hon])
three = create_seg([off, von, off, von, hon, hon, hon])
four = create_seg([von, von, off, von, off, hon, off])
five = create_seg([von, off, off, von, hon, hon, hon])
six = create_seg([von, off, von, von, hon, hon, hon])
seven = create_seg([off, von, off, von, hon, off, off])
eight = create_seg([von, von, von, von, hon, hon, hon])
nine = create_seg([von, von, off, von, hon, hon, off])
nums = [zero, one, two, three, four, five, six, seven, eight, nine]

oos = [0, 3, 6, 9]

tin = st.text_input("Enter a number", "1234")
numbers = [int(x) for x in list(tin)]
print(nums)
for i,d in enumerate(numbers):
    for seg in nums[d]:
        xs = seg[0]
        ys = seg[1]
        if i in [1,3]:
            xs = [x+3 for x in seg[0]]
        if i in [2,3]:
            ys = [y+5 for y in seg[1]]
        ax.plot(xs, ys, color="black")

ax.set_xlim(0, 18)
ax.set_ylim(0, 18)
st.pyplot(fig)
