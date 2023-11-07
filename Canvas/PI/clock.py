"""
control lights and more eventually...
"""

from datetime import datetime
from Tools.Mat import chars, segments
import Tools.Mat as mat
import time
import Tools.setup as pc
from Tools.Temperature import get_temperature

pi = False
if pi:
    import neopixel
    import board

    strip_length = 255
    s1 = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)

if pi:
    # fill in borders and what not
    for p in mat.pixel_outline:
        s1[p] = pc.color_background


def send_char(dplace, number):
    # set everything to zero
    for p in mat.pixels_chars:
        if pi:
            s1[p] = pc.color_off

    p_mat = chars[dplace]  # pixel matrix to loop through
    number_cmd = segments[number]

    # set time
    for i, row in enumerate(p_mat):
        number_row = number_cmd[i]
        for j, pixel in enumerate(row):
            if number_row[j]:
                if pi:
                    s1[pixel] = pc.color_time


def send_sec(seconds):

    # clear all seconds
    for p in mat.sec_pix:
        if pi:
            s1[p] = pc.color_off

    # turn on all seconds that on
    for p in range(seconds):
        if pi:
            s1[mat.sec_pix[p]] = pc.color_sec


temp_time = time.perf_counter()

temp = get_temperature()
temp1 = int(temp//10)
temp2 = int(temp%10)

while True:
    if pi:
        s1.fill([0, 0, 0])
    tn = datetime.now().strftime("%d %H:%M:%S")

    tc = tn[3], tn[4], tn[6], tn[7]
    for i, t in enumerate(tc):
        send_char(i + 1, int(t))

    # determining seconds to send
    secs = int(tn[6:8])
    send_sec(secs)

    # day
    d1 = int(tn[0])
    d2 = int(tn[1])
    # temperature
    et = time.perf_counter() - temp_time
    if et > pc.temp_refresh:
        temp_time = time.perf_counter()
        try:
            temp = get_temperature()
            temp1 = int(temp//10)
            temp2 = int(temp%10)
        except:
            temp = 0

    # sending date and temperature
    for i, d in enumerate([d1, d2, temp1, temp2]):
        print(d)
        send_char(i + 4, d)

    if pi:
        s1.show()
    # date to set

    time.sleep(0.5)
