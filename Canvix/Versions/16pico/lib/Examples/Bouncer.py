"""
Main Cave logic
"""

# bouncing ball game
import time
import lib.Tools.Matrix as mat
from Tools.Hardware import encoder_left, encoder_right, led_strip

class Scene:
    def __init__(self):
        self.rate = .1
        self.v = [1, 1]
        self.vm = [12,10]
        self.tp = [1,1]
        self.p = [1,1]
        self.t = time.monotonic()   # milisecond time stamp

    def loop(self):
        tn = time.monotonic()
        dt = (tn - self.t)*1
        self.t = tn

        # read vx delta
        if encoder_left.delta:
            self.vm[0] += encoder_left.delta
            self.vm[0] = max(self.vm[0], 0)
            self.vm[0] = min(self.vm[0], 20)
            print("vm", self.vm[0])
        if encoder_right.delta:
            self.vm[1] += encoder_right.delta
            self.vm[1] = max(self.vm[1], 0)
            self.vm[1] = min(self.vm[1], 20)
            print("vmy", self.vm[1])

        v = [self.v[0]*self.vm[0], self.v[1]*self.vm[1]]
        self.tp = [self.tp[0]+(v[0]*dt), self.tp[1]+(v[1]*dt)]
        p = self.tp
        p = [round(p[0],0), round(p[1], 0)]
        p = [max(p[0],1), max(p[1], 1)]
        p = [min(p[0],14), min(p[1], 14)]
        p = [int(p[0]), int(p[1])]
        # print(p)

        # make perimeter matrix
        pmat = [
            [p[0]-1, p[1]+1], [p[0], p[1]+1], [p[0]+1, p[1]+1], 
            [p[0]-1, p[1]], [p[0], p[1]], [p[0]+1, p[1]], 
            [p[0]-1, p[1]-1], [p[0], p[1]-1], [p[0]+1, p[1]-1]
        ]

        # loop through and detect if hitting x or y
        if p[0] == 1 and self.v[0]<0:
            self.v[0] = -self.v[0]
        if p[0] == 14 and self.v[0]>0:
            self.v[0] = -self.v[0]
        if p[1] == 1 and self.v[1]<0:
            self.v[1] = -self.v[1]
        if p[1] == 14 and self.v[1]>0:
            self.v[1] = -self.v[1]

        # sending perimeter matrix
        pp = []
        for r in [0,15]:
            for c in range(16):
                pp.append([r,c])
                pp.append([c,r])
  
        led_strip.strip.fill([0,0,0])
        led_strip.send_matrix(pmat, color="Red", show=False)
        led_strip.send_matrix(pp, show=True)

bouncer = Scene()
