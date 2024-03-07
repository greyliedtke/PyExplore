# imports
import neopixel
import board
import time
import board
import math
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

import r.tf

enc_push = DigitalInOut(board.GP22)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

enc = rotaryio.IncrementalEncoder(board.GP21, board.GP20)

def format_2d(f):
    return f"{f:02d}"

count = 0

print("Initiating..1. ")
tn = time.time()
print(tn)
delt = tn - (tn-7200)
days = delt // (24 * 3600)
delt %= 24 * 3600
hours = format_2d(delt // 3600)
minutes = format_2d(delt % 3600 // 60)
seconds = format_2d(delt % 60)
ta = [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]
ta = [int(i) for i in ta]
print(ta)
print(f"Timex: {days}:{hours}:{minutes}:{seconds}")

while True:
    # print("todd 8")
    # print(count * 4)
    count += 1
    time.sleep(1)

