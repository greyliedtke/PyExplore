import neopixel
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

strip_len = 300
led_pin = 0

# np = neopixel.Neopixel(strip_len, 0, led_pin, "GRB")
bp = DigitalInOut(board.GP16)
bp.direction = Direction.INPUT
bp.pull = Pull.UP


red = (255, 0, 0)
hb = 60  # 60 bpm heartbeat

pixel_pin = board.GP0
num_pixels = 300

np = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)


def color_bright(color, brightness):
    # function to set neo pixel to color and brightness
    bp = brightness / 100
    cb = tuple(int(c * bp) for c in color)
    return cb


def pulse():
    # set brightest then fade...
    # print("pulsed")
    tn = time.monotonic()
    for b in range(20, -2, -2):
        
        cc = color_bright(red, b)
        for p in range(num_pixels):
            np[p] = cc
        np.show()
        time.sleep(0.005)
    lt = time.monotonic() - tn
    print('loop time in seconds:', lt)

    


while True:
    if bp.value is False:
        # led.value = False
        pulse()
    # time.sleep(hb / 60)
