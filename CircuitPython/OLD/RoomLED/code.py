import neopixel
import time
import board
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

"""
Setting controls for room led strip
rotary encoder for setting brightness and colors...
set grb? and brightness?

"""

modes = ['R', 'G', 'B', 'Colors', 'Bright']
mode = 0
led_color = [255, 255, 255]


colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]]
color_i = 0

# detect press of encoder
def change_mode(mode):
    mode += 1
    if mode >= len(modes):
        mode = 0
    print(modes[mode])
    time.sleep(.5)
    return mode

def change_color(mode, change, color):
    global color_i, colors
    new_c = color   # default to previous color
    
    if mode in ['R', 'G', 'B']:
        if mode == 'R': ci = 0
        elif mode == 'G': ci = 1
        elif mode == 'B': ci = 2
        new_s = color[ci]+change*10
        if 0 < new_s < 255:
            color[ci] = new_s
            new_c = color

    elif mode == 'Colors':
        new_i = color_i + change
        if new_i == len(colors): color_i=0
        new_c = colors[new_i]

    elif mode == 'Bright':
        # function to set neo pixel to color and brightness
        bp = change / 100
        new_c = [int(c * bp) for c in color]
    
    print(mode, change, color)
    return new_c

# push button
bp = DigitalInOut(board.GP16)
bp.direction = Direction.INPUT
bp.pull = Pull.UP

# rotary encoder
enc = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
ep = 0
op = 0

# led strip
len_pixels = 300
np = neopixel.NeoPixel(board.GP5, len_pixels, auto_write=False)
def set_strip(color):
    for p in range(len_pixels):
        np[p] = color
    np.show()

while True:

    if 0 > enc.position:
        enc.position = 0
    elif enc.position > 10:
        enc.position = 10

    ep = enc.position

    # listen for button to change color mode
    if bp.value is False:
        mode = change_mode(mode)
    
    if op != ep:
        change = op - ep
        led_color = change_color(modes[mode], change, led_color)
        set_strip(led_color)
        op = ep
