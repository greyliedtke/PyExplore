"""
contorl lights and more eventually...
"""

from datetime import datetime
import neopixel
import board

# include brightness by rounding...
strip_length = 60

ng_bright = ui.number("Brightness", value=3)

leds = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)

leds.fill([0,0,10])
leds.show()

