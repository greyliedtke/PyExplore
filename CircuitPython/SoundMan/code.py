"""
used for reading analog input of microphone...

"""
import time
import board
from analogio import AnalogIn
import neopixel

analog_in = AnalogIn(board.A0)
np = neopixel.NeoPixel(board.GP5, 40, auto_write=False)


def send_color(brightness):
    brightness = (brightness/.4)*10

    print(f"br{brightness}")
    color = [brightness * p for p in [255, 0, 0]]
    for i in range(20):
        np[i] = color
    np.show()


def sound_to_color(sound_v):
    mins, maxs = 0, 100
    mapped = (sound_v-mins)/(sound_v-maxs)
    send_color(mapped)


def get_voltage():
    # get voltage out of 100
    return (analog_in.value * 100) / 65536

def sound_detect():
    # read xx samples and return max difference "magnitude"
    max_s = 0
    min_s = 0
    for l in range(1000):
        sound_v = get_voltage()

        max_s = max(sound_v, max_s)
        min_s = min(sound_v, min_s)
    delta = min_s - max_s
    # print(delta)
    av = get_voltage()
    sound_to_color(delta)
    return get_voltage()


while True:
    sound_detect()
    time.sleep(0.05)