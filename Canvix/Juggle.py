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
time_ref = .6
game_l = 16
grav = -.4*time_ref
vyi = 4*time_ref
vxi = 1*time_ref

class Ball:
    def __init__(self):
        self.pos = [2,2]
        self.vy = vyi
        self.vx = vxi

    def next_pos(self):
        if (self.pos[0] <=1 and self.vx<0):
            self.vx = -self.vx
            self.pos[0] = 2
        elif (self.pos[0] >= 14 and self.vx>0):
            self.vx = -self.vx
            self.pos[0] = 13
        self.vy = self.vy + grav
        if self.pos[1] <= 1:
            self.vy = vyi
            self.pos[1] = 1
        self.pos = [self.pos[0]+self.vx, self.pos[1]+self.vy]
        return [round(self.pos[0]), round(self.pos[1],0)]


class Scene:
    def __init__(self):
        self.balls = [Ball()]
        self.b_coords = [[]]

    def loop(self):
        b_coords = []
        for b in self.balls:
            b_coords.append(b.next_pos())
        self.b_coords = b_coords
        return b_coords
jb = Scene()