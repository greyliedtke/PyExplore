# imports

# set pins

# rotary encoder
# led screen
# sound
from support import bound, big_delta
import time
import neopixel
import board
from analogio import AnalogIn
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
from oled import oled_display, oled_text, oled_2_line
oled_text("Grey Room Colors!")


# sound and color mode
modes = ['c/b', 'sound', 'na']
mode_i = 0
colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]]
color_i = 1

enc = rotaryio.IncrementalEncoder(board.GP14, board.GP15)
enc_push = DigitalInOut(board.GP13)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

mic = analog_in = AnalogIn(board.A0)

# led strip
len_pixels = 600
np = neopixel.NeoPixel(board.GP5, len_pixels, auto_write=False)
enc.position=1


while True:

    if mode_i == 0:
        # mode for adjusting brightness with rotary encoder
        enc.position = bound(enc.position)
        brightness = enc.position * 10

    if mode_i == 1:
        # mode for adjusting brightness with audio measurement
        mmax, mmin = 1.6, 1.6
        for m in range(1000):
            mmax, mmin = big_delta(mic.value/65536, mmax, mmin)
        delta = mmax - mmin
        brightness = 100 * delta / 3.3
        
    # hold encoder to change colors
    if not enc_push.value:
        print('pressed')
        time.sleep(.5)
        if not enc_push.value: 
            color_i+=1
            if color_i >= len(colors): color_i=0
    
    # set led strip color
    color_setting = [int(c * brightness) for c in colors[color_i]]
    for p in range(len_pixels):
        np[p] = color_setting
    np.show()
    oled_text(f"{modes[mode_i]}, {brightness}, {colors[color_i]}")





