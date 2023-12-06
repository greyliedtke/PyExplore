"""
control lights and more eventually...
"""

from datetime import datetime
import MatMap.Mat as mat
import time
import MatMap.setup as pc
from MatMap.Temperature import get_temperature
from MatMap.led_strip import strip

# fill in borders and what not
for p in mat.pixel_outline:
    strip[p] = pc.color_background


def send_char(dplace, number):
    # set everything to zero
    for p in mat.pixels_chars:
        strip[p] = pc.color_off

    p_mat = mat.chars[dplace]  # pixel matrix to loop through
    number_cmd = mat.segments[number]

    # set time
    for i, row in enumerate(p_mat):
        number_row = number_cmd[i]
        for j, pixel in enumerate(row):
            if number_row[j]:
                strip[pixel] = pc.color_time


def send_sec(seconds):

    # clear all seconds
    for p in mat.seconds_mat:
        strip[p] = pc.color_off

    # turn on all seconds that on
    for p in range(seconds):
        strip[mat.seconds_mat[p]] = pc.color_sec

temp_time = time.perf_counter()
temp = get_temperature()
temp1 = int(temp//10)
temp2 = int(temp%10)

def clock_set():

    tn = datetime.now().strftime("%d %H:%M:%S")

    tc = tn[3], tn[4], tn[6], tn[7]
    for i, t in enumerate(tc):
        send_char(i + 1, int(t))

    # determining seconds to send
    secs = int(tn[9:11])
    send_sec(secs)

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
    for i, d in enumerate([temp1, temp2]):
        send_char(i + 5, d)

    strip.show()