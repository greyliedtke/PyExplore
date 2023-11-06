"""
control lights and more eventually...
"""

from datetime import datetime
from Tools.Mat import chars, segments
import Tools.Mat as mat
import time
import Tools.setup as pc
from Tools.Temperature import get_temperature

pizero = False
if pizero:
    import neopixel
    import board
    strip_length = 255
    s1 = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)

if pizero:
    # fill in borders and what not
    for p in mat.pixel_outline:
        s1[p] = pc.color_background

def send_char(dplace, number):
    # set everything to zero
    for p in mat.pixels_chars:
        if pizero: s1[p] = pc.color_off

    p_mat = chars[dplace]  # pixel matrix to loop through
    number_cmd = segments[number]

    # set time
    for i, row in enumerate(p_mat):
        number_row = number_cmd[i]
        for j, pixel in enumerate(row):
            if number_row[j]:
                if pizero: s1[pixel] = pc.color_time

def send_sec(seconds):
    for p in mat.sec_pix:
        if pizero: s1[p] = pc.color_off
    for p in range(seconds):
        if pizero: s1[mat.sec_pix[p]] = pc.color_sec

temp_time = time.perf_counter()

while True:
    
    if pizero: s1.fill([0,0,0])
    tn = datetime.now().strftime("%d %H:%M:%S")

    tc = tn[3], tn[4], tn[6], tn[7]
    for i, t in enumerate(tc):
        send_char(i+1, int(t))

    # determining seconds to send
    secs = int(tn[6:8])
    send_sec(secs)

    # day
    d1 = int(tn[0])
    d2 = int(tn[1])
    # temperature
    et = time.perf_counter()-temp_time
    if et > pc.temp_refresh:
        temp_time = time.perf_counter()
        temp = get_temperature()
    
    # sending date and temperature
    for i, d in enumerate([d1, d2, temp]):
        send_char(i+5, d)

    if pizero: s1.show()
    # date to set

    time.sleep(.5)
    
