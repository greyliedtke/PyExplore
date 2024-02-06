"""
main run file 

"""

import lib.globe as g
import lib.matop as mo
from lib.CaveMan import cm as g_cave
from lib.ClockMan import cm as m_clock

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
mode = "clock"
x_data = range(0, g.pw)
fig, ax = plt.subplots()
ax.set_xlim(0, g.pw-1)
ax.set_ylim(0, g.pw-1)

ax.set_yticks([])
sc = ax.scatter(list(x_data), list(x_data))
rd = ax.scatter(0, 8, color='red')

sc.set_offsets(mo.characters[0].char_matrix(4))

def update(frame):
    if mode == "cm":
        m = g_cave.loop()
        sc.set_offsets(np.column_stack(m[0]))
        rd.set_offsets(np.column_stack(m[1]))
    else:
        # clock mode
        m = m_clock.loop()
        # xp = [[p[0] for p in m[0]], [p[1] for p in m[0]]]
        # print(xp)
        sc.set_offsets(m[0])
        rd.set_offsets(np.column_stack(m[1]))


# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=g.refr*1000)

# Show the plot
plt.show()
