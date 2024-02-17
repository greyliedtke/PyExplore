import numpy as np
from MatMap.led_strip import strip

def send_hombre(c1, c2):


    # Define the number of steps in the gradient
    num_steps = 256

    # Create an array of colors transitioning from start_color to end_color
    colors = []

    for i in range(num_steps):
        # Interpolate between start_color and end_color
        r = c1[0] + int((c2[0] - c1[0]) * (i / num_steps))
        g = c1[1] + int((c2[1] - c1[1]) * (i / num_steps))
        b = c1[2] + int((c2[2] - c1[2]) * (i / num_steps))

        # Append the RGB tuple to the colors list
        colors.append((r, g, b))

    for i, color in enumerate(colors):
        strip[i] = color

    strip.show()
