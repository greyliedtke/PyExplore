"""
file for handling hardware encoders
"""

import time
import board
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
        self.delta = 0

    def read(self):
        # push button pressed
        if not self.push.value:
            if not self.pressed:
                print(f"{self.desc}: pushed")
                self.pressed = True
                self.ptime = time.time()
            else:
                htime = time.time() - self.ptime
                if htime > 0.5 and not self.held:
                    print(f"{self.desc}: held")
                    self.held = True
        else:
            self.held = False
            self.pressed = False
        if self.enc.position != self.value:
            print(f"{self.desc}: {self.enc.position}")
            self.delta = self.value - self.enc.position
            self.value = self.enc.position
        else:
            self.delta = 0

encoder_left = Encoder("Left", board.GP2, board.GP1, board.GP0)
encoder_right = Encoder("Right", board.GP5, board.GP4, board.GP3)
# ------------------------------------------------------