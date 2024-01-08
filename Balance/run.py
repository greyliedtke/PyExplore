"""
running servo balancer
"""

# imports
from mpu import read_theta
import time

# var setup
loop_time = .1

class InvertedPendulum:
    def __init__(self):
        self.th1 = 0
        self.th2 = 0
        self.mass = 0
        self.omega = 0.0
        self.alpha = 0.0
        self.tn = time.perf_counter()
        self.dt = 0
    
    def loop(self):
        tn = time.perf_counter()
        self.dt = tn-self.tn
        self.tn = tn

        self.th2 = read_theta()
        if abs(self.th2)>5:
            d_th = self.th_control()
        else:
            d_th = self.pos_control()
        new_th = d_th+self.th1
        send_servo(new_th)

    def th_control(self):
        """
        if th positive, dec serv
        if th negative, inc serv
        do nothing if stable
        """
        d_th = self.th1*.1
        return d_th

    def pos_control(self):
        """
        if th2 <90, dec theta slightly
        if th2 >90, inc theta slightly
        """
        # Update the pendulum state using numerical integration
        d_th = self.th1*.1
        return d_th

ip = InvertedPendulum()

while True:
    try:
        ip.loop()
    except Exception as e:
        print(f"encountered: {e}")