# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import analogio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
time.sleep(.1)
oled_display = init_i2c(board.GP17, board.GP16)
oled_text(oled_display, "GreyMan!")

force_ai = analogio.AnalogIn(board.A0)  # fuel analog input

# force cal
force_lb_v = 2000
b = 0
# 0 = 270
# 10 = 912
# 15 = 1150
# 20 = 1440



def read_force():
    # get analog voltage
    v = force_ai.value
    force = v/force_lb_v - b
    return force


max_f = 0

print("Running Loop")
while True:
    time.sleep(0.2)
    force = read_force()
    max_f = max(max_f, force)
    oled_2_line(oled_display, f"Force: {force}", f"Max: {max_f}")
