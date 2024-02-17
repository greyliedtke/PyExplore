"""
Main Cave logic
"""

# pygame tunnel run
import numpy as np
from collections import deque
import time
import math


# constants
# velocites in Pixels per second
scale = 1
game_l = 16
grav = -22
vyi = 4*scale
vxi = 2*scale

t_air = 2
vyi = -.5*grav*t_air
vxi = (game_l-2)/t_air

class Ball:
    def __init__(self, start_pos = [8,8], vxi = vxi, vyi = vyi):
        self.pos = start_pos
        self.bb = [[0,0,0,0],[0,0,0,0]]
        self.bound_box(self.pos[0],self.pos[1])
        self.vy = vyi
        self.vx = vxi
        self.left = self.bb[0][0]
        self.right = self.bb[2][0]
        self.top = self.bb[0][1]
        self.bottom = self.bb[1][1]

    def next_pos(self, et):

        # horizontal bounds
        self.left = self.bb[0][0]
        self.right = self.bb[2][0]
        self.top = self.bb[0][1]
        self.bottom = self.bb[1][1]

        if (self.left <=1 and self.vx<0):
            self.vx = -self.vx
            self.pos[0] = 1
        elif (self.right >= 15 and self.vx>0):
            self.vx = -self.vx
            self.pos[0] = 15
        self.vy = self.vy + grav*et
        
        # vertical bounds lower box hits
        if self.bottom <= 1:
            self.vy = vyi
            self.pos[1] = 1
        self.pos = [self.pos[0]+self.vx*et, self.pos[1]+self.vy*et]
        self.bound_box(self.pos[0],self.pos[1])
        return self.bb

    def bound_box(self, x,y):
        x1 = math.floor(x)
        x2 = math.ceil(x)
        if x1 == x2:
            x2 += 1
        y1 = math.floor(y)
        y2 = math.ceil(y)
        if y1 == y2:
            y2 += 1
        self.bb = [[x1,y1], [x1, y2], [x2, y1], [x2, y2]]
        return self.bb

class Scene:
    def __init__(self):
        self.balls = [Ball([1,1]), Ball([15,1], vxi=-vxi)]
        self.balls = [Ball([1,1])]
        self.b_coords = [[]]
        self.it = time.perf_counter()

    def collision(self):
        b1 = self.balls[0]
        b2 = self.balls[1]
        if abs(b1.pos[0]-b2.pos[0])<2:
            if abs(b1.pos[1]-b2.pos[1])<2:
                b1v = [b1.vx, b1.vy]
                b2v = [b2.vx, b2.vy]
                b2.vx, b2.vy = b1v[0], b1v[1]
                b1.vx, b1.vy = b2v[0], b2v[1]

    def loop(self):
        # self.collision()
        time_now = time.perf_counter()
        et = time.perf_counter()-self.it
        self.it = time_now

        for b in self.balls:
            b.next_pos(et)
jb = Scene()