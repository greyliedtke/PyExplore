"""
file for handling globals
"""

import time
import keyboard

# main info for setup
pw = 16
ti = time.perf_counter()
refr = .1

# rotary encoder...
# use keyboard to simulate 
def move_delta():
    if keyboard.is_pressed('left'):
        delta = -1
    elif keyboard.is_pressed('right'):
        delta = 1
    else:
        delta = 0
    return delta


# neostrip
# brightness
