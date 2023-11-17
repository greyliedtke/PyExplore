# imports
import neopixel
import board

colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]]
color_i = 1

# led strip
len_pixels = 600
strip = neopixel.NeoPixel(board.GP0, len_pixels, auto_write=False)
strip.brightness = .1

strip[1] = colors[color_i]
strip.show()

