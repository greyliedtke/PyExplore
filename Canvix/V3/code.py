"""
main run file 
lib references


"""

import lib.Tools.Hardware as hard
import lib.Tools.Matrix as mat
from lib.Examples.CaveMan import cm as g_cave
from lib.Examples.ClockMan import cm as m_clock
from lib.Examples.CubeMan import cm as m_cube

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
mode = "cube"
x_data = range(0, hard.pw)
fig, ax = plt.subplots()
ax.set_xlim(0, hard.pw-1)
ax.set_ylim(0, hard.pw-1)

ax.set_yticks([])
sc = ax.scatter(list(x_data), list(x_data))
rd = ax.scatter(0, 8, color='red')

sc.set_offsets(mat.characters[0].char_matrix(4))

def update(frame):
    if mode == "cm":
        m = g_cave.loop()
        sc.set_offsets(m[0])
        rd.set_offsets(m[1])
    if mode == "cube":
        m = m_cube.loop()
        sc.set_offsets(m)
    else:
        # clock mode
        m = m_clock.loop()
        # xp = [[p[0] for p in m[0]], [p[1] for p in m[0]]]
        # print(xp)
        sc.set_offsets(m[0])


# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=hard.refr*1000)

# Show the plot
plt.show()
