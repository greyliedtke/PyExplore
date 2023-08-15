# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import analogio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
time.sleep(2)
oled_display = init_i2c(board.GP13, board.GP12)
oled_text(oled_display, "GreyMan!")

force_ai = analogio.AnalogIn(board.A0)  # fuel analog input

# force cal
force_lb_v = 100 / 2122


def read_force():
    # get analog voltage
    v = force_ai.value
    force = v * force_lb_v
    return force


max_f = 0

print("Running Loop")
while True:
    time.sleep(0.2)
    force = read_force()
    oled_2_line(oled_display, f"Force: {force}", f"Max: {max(max_f, force)}")
