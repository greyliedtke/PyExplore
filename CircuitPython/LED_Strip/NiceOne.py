"""
creating simple led controlling device
"""

import rotaryio
from oled import oled_text, oled_2_line, init_i2c
import neopixel
import board
from digitalio import DigitalInOut, Direction, Pull

# LED SCREEN
oled_display = init_i2c(board.GP17, board.GP16)
oled_text(oled_display, "GreyMan!")

# INITIALIZE PIXELS
len_pixels = 300
np = neopixel.NeoPixel(board.GP0, len_pixels, auto_write=False)

# ROTARY ENCODER
enc = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
enc_push = DigitalInOut(board.GP8)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

# COLORS
d_colors = {
    "red":[255, 0, 0],
    "green":[0, 255, 0],
    "blue":[0, 0, 255],
    "white":[255, 255, 255],
}
colors = list(d_colors.keys())

# CHANGE BRIGHTNESS 
def scale_brightness(bright_int, a_rgb):
    bright_fact = bright_int / 5
    new_a_rgb = [int(b * bright_fact) for b in a_rgb]
    return new_a_rgb
    # normal

# NEXT COLOR
def next_color(i_color):
    i_color+=1
    if i_color >= len(colors):
        i_color = 0
    return colors[i_color]


# LOOP LOGIC
c = next_color(0)
n = scale_brightness(5, d_colors[c])

# ---
# LOOP LOGIC
# ---
