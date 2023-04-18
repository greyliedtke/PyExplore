# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rotaryio
from oled import oled_text, oled_2_line, init_i2c
import neopixel

# Initializing display
gnd_oled = DigitalInOut(board.GP13)
gnd_oled.direction = Direction.OUTPUT
gnd_oled.value = False
v_oled = DigitalInOut(board.GP12)
v_oled.direction = Direction.OUTPUT
v_oled.value = True
time.sleep(2)
oled_display = init_i2c(board.GP11, board.GP10)
oled_text(oled_display, "GreyMan!")

# setting up rotary encoder
v_enc = DigitalInOut(board.GP9)
v_enc.direction = Direction.OUTPUT
v_enc.value = True
enc = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
enc_push = DigitalInOut(board.GP8)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

# setting up neopixel strip
# led strip
len_pixels = 300
np = neopixel.NeoPixel(board.GP0, len_pixels, auto_write=False)
np[55] = [255, 0, 0]
np.show()

while True:
    for x in range(1000):
        oled_2_line(oled_display, f"count: {x}", f"encoder: {enc.position}")
        time.sleep(.1)


