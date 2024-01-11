"""
# script for setting pixels
"""

import neopixel
import board

strip_length = 256
strip = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)
strip.brightness = .1
