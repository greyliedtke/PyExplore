"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
import lib.Tools.Hardware as hw
from lib.Tools.Colors import color_dict, colors

class Scene:
    def __init__(self):
        self.cursor = [8,8]
        self.active = False
        self.blink = False
        self.color = colors[0]
        self.trace = {}

    def update_location(self):
        # update location with max change of 1 and range of 0-15
        dx, dy = hw.move_delta()
        dx = min(1, max(-1, dx))
        dy = min(1, max(-1, dy))
        new_x = self.cursor[0] + dx
        new_y = self.cursor[1] + dy
        new_x = min(15, max(0, new_x))
        new_y = min(15, max(0, new_y))
        self.cursor = (new_x, new_y)
        self.trace[self.cursor] = self.color

    def loop(self):

        # toggle cursor
        if self.blink:
            pass
        self.blink = not self.blink

        if hw.knob_1:
            # change color
            pass
        if hw.knob_2:
            # toggle draw mode
            if self.active: self.active = False
            else: self.active = True
        if hw.knob_2_held:
            self.trace = {}
            pass
            # clear canvas

        
cm = Scene()