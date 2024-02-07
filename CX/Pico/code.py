"""
main run file 
...globals
"""

import time
import random
import neopixel
import board
import math
import rotaryio
from digitalio import DigitalInOut, Direction, Pull


# ------------------------------------------------------
# encoder setups
class Encoder:
    def __init__(self, desc, pin1, pin2, pin_push):
        self.desc = desc
        self.enc = rotaryio.IncrementalEncoder(pin1, pin2)
        self.enc.position = 0
        self.push = DigitalInOut(pin_push)
        self.push.direction = Direction.INPUT
        self.push.pull = Pull.UP
        self.value = 0
        self.pressed = False
        self.held = False
        self.ptime = 0

    def read(self):
        # push button pressed
        if not self.push.value:
            if not self.pressed:
                print(f"{self.desc}: pushed")
                self.pressed = True
                self.ptime = time.time()
            else:
                htime = time.time() - self.ptime
                if htime > .5 and not self.held:
                    print(f"{self.desc}: held")
                    self.held = True
        else:
            self.held = False
            self.pressed = False
        if self.enc.position != self.value:
            print(f"{self.desc}: {self.enc.position}")
            self.value = self.enc.position

enc_1 = Encoder('1', board.GP3, board.GP4, board.GP5)
enc_2 = Encoder('2', board.GP6, board.GP7, board.GP8)

while True:
    enc_1.read()
    enc_2.read()
    if enc_1.held and enc_2.held:
        print("both held")
    time.sleep(.1)