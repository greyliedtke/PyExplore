import board, digitalio, busio, time, displayio, rgbmatrix, framebufferio
import adafruit_imageload, terminalio, random
import adafruit_display_text.label as label


displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, bit_depth=2, tile=1, serpentine=True,
    rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],
    addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20, board.GP22],
    clock_pin=board.GP11, latch_pin=board.GP12, output_enable_pin=board.GP13)

display = framebufferio.FramebufferDisplay(matrix)
splash = displayio.Group()

matrix.brightness = .001

line_1 = label.Label(terminalio.FONT, text="Jeanne the", color=0xf7fa32, x=1, y=1)
line_2 = label.Label(terminalio.FONT, text="GOAT", color=0x92d982, x=1, y=16)
line_1.append(line_2)
display.show(line_1)
time.sleep(.10)

matrix.brightness = .01

line_1 = label.Label(terminalio.FONT, text="Jeanne the", color=0xf7fa32, x=1, y=1)
line_2 = label.Label(terminalio.FONT, text="GOAT", color=0x92d982, x=1, y=16)
line_1.append(line_2)
display.show(line_1)
time.sleep(.1)

import adafruit_imageload

image, palette = adafruit_imageload.load(
    "g1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette
)
# image, palette = adafruit_imageload.png.load(
#     "bsmall.png", bitmap=displayio.Bitmap, palette=displayio.Palette
# )
tile_grid = displayio.TileGrid(image, pixel_shader=palette)

# # Create a TileGrid to hold the bitmap
# tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)
display.show(group)
time.sleep(10)




