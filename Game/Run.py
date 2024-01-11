import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from CaveMan import cm, game_l
from PingMan import pm

# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
x_data = range(0, game_l)
fig, ax = plt.subplots()
ax.set_xlim(0, game_l)
ax.set_ylim(0, game_l)
ax.set_title("CanvArt")
ax.set_xticks([])
ax.set_yticks([])
sc = ax.scatter(x_data, x_data)
rd = ax.scatter(0, 8, color='red')
# ------------------------------------------------------

# game mode
game_mode = "Ping"

# Function to update the scatter plot
def update(frame):
    if game_mode == "CaveMan":
        cave_matrix = cm.loop()
        sc.set_offsets(np.column_stack(cave_matrix))
        rd.set_offsets([cm.body, 1])
    if game_mode == "Ping":
        pm.loop()
        sc.set_offsets(pm.ping)

        rd.set_offsets(np.column_stack(pm.pp))


        

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the plot
plt.show()
