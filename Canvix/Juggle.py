"""
Main Cave logic
"""

# pygame tunnel run
import numpy as np
import random
from collections import deque
import keyboard
import time
import math


# constants
time_ref = .6
game_l = 16
grav = -.4*time_ref
vyi = 4*time_ref
vxi = .5*time_ref

class Ball:
    def __init__(self, start_pos = [8,8]):
        self.pos = start_pos
        self.bb = [[0,0,0,0],[0,0,0,0]]
        self.bound_box(self.pos[0],self.pos[1])
        self.vy = vyi
        self.vx = vxi
        self.left = self.bb[0][0]
        self.right = self.bb[2][0]
        self.top = self.bb[0][1]
        self.bottom = self.bb[1][1]

    def collision(self):
        # detect walls
        # detect other balls
        # change velocities
        pass


    def next_pos(self):

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
        self.vy = self.vy + grav
        
        # vertical bounds lower box hits
        if self.bottom <= 1:
            self.vy = vyi
            self.pos[1] = 1
        self.pos = [self.pos[0]+self.vx, self.pos[1]+self.vy]
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
        self.balls = [Ball([1,2]), Ball([14,2])]
        self.b_coords = [[]]

    def loop(self):

        b = self.balls[0]
        ob = self.balls[1]

        if b.left == ob.right or b.right == ob.left:
            if b.top in [ob.top, ob.bottom] or b.bottom in [ob.top, ob.bottom]:
                vx1, vx2 = b.vx, ob.vx

                b.vx = vx2
                b.pos[0] = b.pos[0]+b.vx
                ob.vx = -vx1
                ob.pos[0] = ob.pos[0]+ob.vx

        for i,b in enumerate(self.balls):
            b.next_pos()
            # for j,ob in enumerate(self.balls):
            #     if i == j: continue
jb = Scene()