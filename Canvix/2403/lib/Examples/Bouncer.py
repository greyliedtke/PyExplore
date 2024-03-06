"""
Main Cave logic
"""

# bouncing ball game
import time
import lib.Tools.Matrix as mat
from Tools.Hardware import encoder_left, encoder_right, led_strip


# Define LED matrix dimensions
rows = 16
cols = 16


class Scene:
    def __init__(self):
        self.rate = .1
        self.v = [0, 0]
        self.pos = [0,0]
        self.t = time.time()

    def loop(self):
        tn = time.time()
        dt = tn - self.t
        self.t = tn

        # read vx delta
        self.v[0] = encoder_left.read_delta()
        self.v[1] = encoder_right.read_delta()

        p = [self.pos[0]+(self.v[0]*dt) + self.pos[1]+(self.v[1]*dt)]
        p = [round(p[0],0), round(p[1], 0)]
        p = [max(p[0],0), max(p[1], 0)]
        p = [min(p[0],15), min(p[1], 15)]

        # make perimeter matrix
        pmat = [
            [p[0]-1, p[1]+1], [p[0], p[1]+1], [p[0]+1, p[1]+1], 
            [p[0]-1, p[1]], [p[0], p[1]], [p[0]+1, p[1]], 
            [p[0]-1, p[1]-1], [p[0], p[1]-1], [p[0]+1, p[1]-1]
        ]

        xs = [x[0] for x in pmat]
        ys = [x[1] for x in pmat]

        # loop through and detect if hitting x or y
        for x in xs:
            if x in [0,16]:
                self.v[0] = -self.v[0]
        for y in ys:
            if y in [0,16]:
                self.v[1] = -self.v[1]

        led_strip.wipe()
        pa = mat.
        led_strip.send_array()
        
            
        return projected_cube


cm = Scene()
