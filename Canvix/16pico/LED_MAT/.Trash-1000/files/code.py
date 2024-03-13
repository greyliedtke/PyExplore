"""
script to operate pi pico as led matrix controller

Modes:
- sine wave
- rain
- random dots
- static images
"""

import time
import random
import neopixel
import board
import math
from interp import point_make
from Mat import xy_mat
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

enc_push = DigitalInOut(board.GP22)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP
enc = rotaryio.IncrementalEncoder(board.GP21, board.GP20)
s1 = neopixel.NeoPixel(board.GP2, 300, auto_write=False, brightness=.1)
enc.position = 4


def send_sine(amplitude, frequency, offset):
    if enc_push.value == False:
        print(enc.position)
    # clear strip
    s1.fill([0, 0, 0])

    x = list(range(15))
    y = [8 + enc.position * math.sin(frequency * xr + offset) for xr in x]

    a_x, a_y = [], []
    for i in range(len(x)):
        eq_x, eq_y = point_make(x[i], y[i])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_y.append(eq_y[0])
        a_y.append(eq_y[1])
        a_y.append(eq_y[1])
        a_y.append(eq_y[0])

    for i, p in enumerate(a_x):
        print(a_x[i], a_y[i])
        pix = xy_mat(a_x[i], a_y[i])
        s1[pix] = [0, 10, 10]

    s1.show()


def sine_animation():
    ti = time.monotonic()

    while True:
        ts = time.monotonic() - ti
        # send_sine(3, 0.7, ts * 2.5)
        send_sine(7, 0.45, ts * 3.14 * 0.7)  # 1 wave
        # send_sine(5, 0.9, ts * 3.14 * 0.7)


sine_animation()


# creating animation of bouncing cube
def wall_bouncer():
    vx = 1
    vy = 1
    x = 8
    y = 0
    while True:
        x = x + vx
        y = y + vy

        if x == 16:
            x -= 2
            vx = -vx
        elif x == 0:
            x += 2
            vx = -vx
        if y >= 16:
            y -= 2
            vy = -vy
        elif y == 0:
            y += 2
            vy = -vy

        print(x, y)
        pix = xy_mat(x, y)
        s1.fill([0, 0, 0])
        s1[pix] = [0, 20, 21]
        s1.show()
        time.sleep(0.2)


wall_bouncer()
