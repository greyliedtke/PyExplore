"""
creating simple led controlling device
"""

import neopixel
import board
import time

# INITIALIZE PIXELS
s1_len = 60
s1 = neopixel.NeoPixel(board.GP0, s1_len, auto_write=False)
pixel_range = range(10,50)

def lerp(start_color, end_color, t):
    """Linear interpolation between two RGB colors."""
    r = int(start_color[0] + t * (end_color[0] - start_color[0]))
    g = int(start_color[1] + t * (end_color[1] - start_color[1]))
    b = int(start_color[2] + t * (end_color[2] - start_color[2]))
    return (r, g, b)

# color controls
# red, green, blue
color_a = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
color_i = 0
count = 0

# time to change color
t_loop = 60 # seconds
num_steps = 60 # Number of steps in the transition
t_delay = t_loop/num_steps  # Time between each step (in seconds)

while True:
    count+=1
    
    if color_i == len(color_a):
        color_i = 0
    
    c1 = color_a[color_i]

    if color_i == len(color_a)-1:
        c2 = color_a[0]
    else:
        c2 = color_a[color_i+1]
    
    color_i += 1

    for step in range(num_steps):
        t = step / (num_steps - 1)
        interpolated_color = lerp(c1, c2, t)

        s1.fill(interpolated_color)
        s1.show()

        time.sleep(t_delay)