import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from CaveMan import cm, game_l
from PingMan import pm
from ClockMan import clock
from MatMap.Mat import characters
from Juggle import jb

# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
x_data = range(0, game_l)
fig, ax = plt.subplots()
ax.set_xlim(0, game_l)
ax.set_ylim(0, game_l)

ax.set_yticks([])
sc = ax.scatter(x_data, x_data)
rd = ax.scatter(0, 8, color='red')
# ------------------------------------------------------

# game mode
game_mode = "Juggle"

# Function to update the scatter plot
def update(frame):
    if game_mode == "CaveMan":
        cave_matrix = cm.loop()
        sc.set_offsets(np.column_stack(cave_matrix))
        rd.set_offsets([cm.body, 1])
    elif game_mode == "Ping":
        pm.loop()
        sc.set_offsets(pm.ping)
        rd.set_offsets(np.column_stack(pm.pp))
    elif game_mode == "Clock":
        clock.loop()
        sc.set_offsets(clock.time_mat)
        rd.set_offsets(np.column_stack(clock.deg_mat))

    elif game_mode == "Char":
        mx, my = [], []
        for i in range(8):
            matrix = characters[i].char_matrix(i)
            mx += matrix[0]
            my += matrix[1]
        sc.set_offsets(np.column_stack([mx,my]))
    elif game_mode == "Juggle":
        mx, my = [], []
        jb.loop()
        bx, by = jb.b_coords[0][0], jb.b_coords[0][1]
        sc.set_offsets([bx,by])     

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=100)

# Show the plot
plt.show()
