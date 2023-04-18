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
colors = {
    "red":[255, 0, 0], 
    "green": [0, 255, 0], 
    "blue": [0, 0, 255], 
    "white": [255, 255, 255]
}
color_a = list(colors.values())
colors_l= list(colors.keys())
color_i = 0

len_pixels = 300
np = neopixel.NeoPixel(board.GP0, len_pixels, auto_write=False)

def set_pixels(color_i):
    brightness = abs(enc.position/100)
    color_setting = [int(c * brightness) for c in color_a[color_i]]
    print(color_setting)
    for p in range(len_pixels):
        np[p] = color_setting
    np.show()

print('Running Loop')
while True:

    time.sleep(.1)
    oled_2_line(oled_display, f"color: {colors_l[color_i]}", f"brightness: {enc.position}")

    if enc_push.value == False:
        print(f"okay")
        set_pixels(color_i)
        time.sleep(1)
        if enc_push.value == False:
            print(f"dobulet ok")
            color_i +=1
            set_pixels(color_i)
            


