"""
Main Cave logic
"""

# pygame tunnel run
import numpy as np
import random
from collections import deque
import keyboard
import time


# constants
game_l = 16
wall_t = 3
cave_w = 2 # size of cave hole
middle = int(game_l/2)  # middle of canvas
og_cave = [middle for i in range(game_l)]

class Scene:
    def __init__(self):
        self.rate = .25
        self.it = time.perf_counter()
        self.time_q = []
        self.n2 = []

    def loop(self):
        # updating cave setpoint
        et = time.perf_counter()-self.it
        self.time_q.append(et)

        self.n2.append(et*2)

        # controlling game
        if keyboard.is_pressed('up'):
            print("power_up")
        elif keyboard.is_pressed('down'):
            print("power_down")
        elif keyboard.is_pressed('u'):
            print("pr_up")
        elif keyboard.is_pressed('j'):
            print("pr_down")

turboSim = Scene()