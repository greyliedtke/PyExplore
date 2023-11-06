"""
control lights and more eventually...
"""

from datetime import datetime
from Tools.Mat import digits, segments
import time

pizero = True
if pizero:
    import neopixel
    import board
    strip_length = 255
    s1 = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)

def time_send(dplace, number):
    # set everything to zero

    p_mat = digits[dplace]  # pixel matrix to loop through
    number_cmd = segments[number]

    for i, row in enumerate(p_mat):
        number_row = number_cmd[i]
        for j, pixel in enumerate(row):
            if number_row[j]:
                if pizero:
                    s1[pixel] = [0,0,10]
                    

def clock_setting():
    tn = datetime.now().strftime("%H:%M:%S")

    tc = tn[0], tn[1], tn[3], tn[4]
    for i, t in enumerate(tc):
        time_send(i+1, int(t))


while True:
    s1.fill([0,0,0])
    clock_setting()
    time.sleep(1)
    s1.show()
