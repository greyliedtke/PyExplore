"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
from lib.Tools.Hardware import led_strip, encoder_left
import random
import lib.Tools.Colors as colors



# Define the number of steps in the gradient
def color_change(start_color, end_color):
    num_steps = 16

    # Create an array of colors transitioning from start_color to end_color
    colors = []

    for i in range(num_steps):
        # Interpolate between start_color and end_color
        r = start_color[0] + int((end_color[0] - start_color[0]) * (i / num_steps))
        g = start_color[1] + int((end_color[1] - start_color[1]) * (i / num_steps))
        b = start_color[2] + int((end_color[2] - start_color[2]) * (i / num_steps))
        c_ints = [int(c) for c in [r,g,b]]
        # Append the RGB tuple to the colors list
        for r in range(16):
            colors.append(c_ints)
    return colors

class Scene:
    def __init__(self):
        self.g = 0
        self.color = colors.random_color()
        self.cq = self.new_color_transition()
        self.modes = ["color_fade", "mat_transition"]
        self.mode = 0
        self.time = time.time()

    def new_color_transition(self):
        start_color = self.color
        end_color = colors.random_color()
        ca = []

        num_steps = 100
        for i in range(num_steps):
            # Interpolate between start_color and end_color
            r = start_color[0] + int((end_color[0] - start_color[0]) * (i / num_steps))
            g = start_color[1] + int((end_color[1] - start_color[1]) * (i / num_steps))
            b = start_color[2] + int((end_color[2] - start_color[2]) * (i / num_steps))
            c_ints = [int(c) for c in [r,g,b]]
            ca.append(c_ints)
        self.cq = ca
        return ca

    def mode_color_fade(self):
        self.color = self.cq[0]
        led_strip.flash(self.color)
        if len(self.cq)== 1:
            self.new_color_transition()
        else:
            self.cq.pop(0)
        # time.sleep(.001)

    def mode_mat_transition(self):
        et = time.time()-self.time
        if et > 2:
            c1 = colors.random_color()
            c2 = colors.random_color()
            p_a = color_change(c1, c2)
            led_strip.send_strip(p_a)
            self.time = time.time()

    def loop(self):
        encoder_left.read()
        if encoder_left.held:
            self.mode+=1
            if self.mode==len(self.modes):
                self.mode=0
            print(self.mode)
            print(self.modes[self.mode])
        if self.mode == 0:
            self.mode_mat_transition()
        elif self.mode == 1:
            self.mode_color_fade()

colorfade = Scene()
