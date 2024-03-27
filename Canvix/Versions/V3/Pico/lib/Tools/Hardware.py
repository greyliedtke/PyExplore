"""
file for handling hardware
"""

import time
import random
import neopixel
import board
import math
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

# ------------------------------------------------------
# LED Strip
class LED_Strip:
    def __init__(self):
        # bright = 0.025
        bright = 1
        self.strip = neopixel.NeoPixel(board.GP0, 256, auto_write=False, brightness=bright)

    def flash(self):
        self.strip.fill([0,170,221])
        self.strip.show()

    def wipe(self):
        self.strip.fill([0,0,0])
        self.strip.show()

    def send_array(self, pixel_a):
        self.strip.fill([0,0,0])
        for p in pixel_a:
            self.strip[p] = [0,170,221]
        self.strip.show()
led_strip = LED_Strip()


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

    def read_delta(self):
        t_delta = self.enc.position - self.value
        self.value = self.enc.position
        if t_delta>5 or t_delta<-5:
            t_delta = t_delta*60
        return t_delta

enc_1 = Encoder('1', board.GP3, board.GP4, board.GP5)
enc_2 = Encoder('2', board.GP6, board.GP7, board.GP8)

# neostrip
# brightness
