"""
script to operate pi pico as led matrix controller

Modes:
- sine wave
- rain
- random dots
- static images

button press will
- increment animation
- reset knob

- sine wave
- bouncing ball
- solar system
- rain

- games
- snake
- pong

"""

# ------------------------------------------------------
# imports
import time
import random
import neopixel
import board
import math
from interp import point_make
from Mat import xy_mat
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
from Strip import s
from sine import send_sine
from bounce import bw
# ------------------------------------------------------

# ------------------------------------------------------
# initialize hardware
class RotEnc:
    def __init__(self):
        self.mode = 0
        self.enc = rotaryio.IncrementalEncoder(board.GP21, board.GP20)
        self.v = self.enc.position
        self.mm = [0,10]
        self.butt = DigitalInOut(board.GP22)
        self.butt.direction = Direction.INPUT
        self.butt.pull = Pull.UP

    def bound(self):
        if self.v > self.mm[1]:
            self.v = self.mm[1]
        if self.v < self.mm[0]:
            self.v = self.mm[0]
re = RotEnc()

# ------------------------------------------------------

# ------------------------------------------------------
# buttons and colors
modes = ["sine", "rain", "random", "static"]
mode_i = 0
mode = modes[mode_i]

colors = ["red", "green", "blue"]
color_i = 0
color = colors[color_i]
# ------------------------------------------------------

# ------------------------------------------------------
# variables
ti = time.perf_counter()    # track time
# ------------------------------------------------------

# ------------------------------------------------------
# Main control loop
while True:
    re.bound()
    te = time.perf_counter()-ti    # track time
    s.fill([0,0,0])

    if mode == "sine":
        amp = re.v
        send_sine(amp, 0.45, te * 3.14 * 0.7)
    elif mode == "bounce":
        bw.loop()

    if re.butt.value == False:
        mode_i += 1
        if mode_i > len(modes) - 1:
            mode_i = 0
        mode = modes[mode_i]
        print(mode)
# ------------------------------------------------------
