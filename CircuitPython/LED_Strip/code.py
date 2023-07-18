"""
creating simple led controlling device
"""

import rotaryio
import neopixel
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# INITIALIZE PIXELS
s1_len = 60
s1 = neopixel.NeoPixel(board.GP0, s1_len, auto_write=False)
s2_len = 300
s2 = neopixel.NeoPixel(board.GP2, s2_len, auto_write=False)

# ROTARY ENCODER
enc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)
enc_push = DigitalInOut(board.GP20)
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
    print(new_a_rgb)
    return new_a_rgb
    # normal

# NEXT COLOR
def next_color(i_color):
    i_color+=1
    if i_color >= len(colors):
        i_color = 0
    print(d_colors[colors[i_color]])
    return i_color

# ---
# SEND STRIP
def send_color(a_rgb):
    s1.fill(a_rgb)
    s2.fill(a_rgb)
    s1.show()
    s2.show()


# ---
# Globals
v_color = 0
v_bright = 2
enc.position = v_bright
v_color_a = d_colors[colors[v_color]]
# ---

# ---
# Bound encoder
def enc_bound():
    if enc.position < 0: enc.position=0
    if enc.position > 5: enc.position=5
# ---

# LOOP LOGIC
while True:
    time.sleep(.1)
    enc_bound()
    if enc.position != v_bright:
        v_bright = enc.position
        v_color_a = scale_brightness(v_bright, d_colors[colors[v_color]])
    if not enc_push.value:
        v_color = next_color(v_color)
        v_color_a = d_colors[colors[v_color]]
        time.sleep(.5)
    send_color(v_color_a)
    
