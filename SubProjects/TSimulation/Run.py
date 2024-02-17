import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from TSim import turboSim

# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
data_len = 30
x_data = range(0, data_len)
fig, ax = plt.subplots(3,1)

ax[1].set_ylim(0, 15)
sc,  = ax[0].plot(x_data, x_data)
sc2,  = ax[1].plot(x_data, x_data)
# ------------------------------------------------------

# Function to update the scatter plot
def update(frame):
    turboSim.loop()
    if len(turboSim.time_q) > data_len:
        ax[0].set_xlim(min(turboSim.time_q[-data_len:-1]), max(turboSim.time_q[-data_len:-1]))
        ax[0].set_ylim(min(turboSim.n2[-data_len:-1]), max(turboSim.n2[-data_len:-1]))
    sc.set_xdata(turboSim.time_q)
    sc.set_ydata(turboSim.n2)

    sc2.set_xdata(turboSim.time_q)
    sc2.set_ydata(turboSim.n2)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the plot
plt.show()
