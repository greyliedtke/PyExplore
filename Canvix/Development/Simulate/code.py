"""
main run file 
lib references

"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sine_wave


# ------------------------------------------------------
# Initialize the figure that would be led matrix
# Create some random data
mode = "cube"
length = 64
x_data = range(0, 64)
fig, ax = plt.subplots()
ax.set_xlim(0, length)
ax.set_ylim(0, length)

ax.set_yticks([])
sc = ax.scatter(list(x_data), list(x_data))
rd = ax.scatter(0, 8, color='red')

x,y = sine_wave.send_sine(30, .1, 0)
sc = ax.scatter(x, y)
x,y = sine_wave.send_sine(15, .2, 0)
sc = ax.scatter(x, y)


# sc.set_offsets(mat.characters[0].char_matrix(4))

def update(frame):
    print('loop')

# Create the animation
# ani = FuncAnimation(fig, update, frames=range(100), interval=500)

# Show the plot
plt.show()
