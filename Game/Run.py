import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from CaveMan import cm, game_l

# ------------------------------------------------------
# Initialize the figure
# Create some random data
x_data = range(0, game_l)
fig, ax = plt.subplots()
ax.set_xlim(0, game_l)
ax.set_ylim(0, game_l)
sc = ax.scatter(x_data, x_data)
rd = ax.scatter(0, 8, color='red')
# ------------------------------------------------------

# Function to update the scatter plot
def update(frame):
    cave_matrix = cm.loop()

    # Update the data in
    # dot = np.random.randint(0, game_w)
    # rd.set_offsets([dot, 1])
    cavex = [item for sublist in cave_matrix[0] for item in sublist]
    cavey = [item for sublist in cave_matrix[1] for item in sublist]
    cave_matrix = [cavex, cavey]

    sc.set_offsets(np.column_stack(cave_matrix))
    rd.set_offsets([cm.body, 1])
    

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the plot
plt.show()
