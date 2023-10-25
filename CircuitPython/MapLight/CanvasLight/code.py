# sudo chmod a+rw /dev/ttyACM0

# neopixel strip

import neopixel
import board
import time
import random
from pclock import digits, segments


# INITIALIZE PIXELS
s1_len = 256
s1 = neopixel.NeoPixel(board.GP0, s1_len, auto_write=False)

# COLORS
d_colors = {"red": [9, 4, 1], "blue": [1, 4, 9]}
cc = "blue"


mins = 0

s1.fill([0, 0, 0])
s1.show()


def time_send(dplace, number):
    # set everything to zero

    p_mat = digits[dplace]  # pixel matrix to loop through
    number_cmd = segments[number]

    for i, row in enumerate(p_mat):
        print(i)
        number_row = number_cmd[i]
        # print(row)
        # print(number_row)
        for j, pixel in enumerate(row):
            print(j)
            if number_row[j]:
                print(pixel)
                s1[pixel] = d_colors[cc]
                s1.show()


mya = range(256)

b_time = 2
p_time = 1

while True:
    while True:
        p_array = list(mya)

        for p in range(s1_len):
            random_index = random.randint(0, len(p_array)) - 1
            # Remove the element at the random index
            removed_value = p_array.pop(random_index)
            s1[removed_value] = d_colors[cc]
            s1.show()
            time.sleep(p_time)

        time.sleep(b_time)

        p_array = list(mya)

        for p in range(s1_len):
            random_index = random.randint(0, len(p_array)) - 1
            # Remove the element at the random index
            removed_value = p_array.pop(random_index)
            s1[removed_value] = (0, 0, 0)
            s1.show()
            time.sleep(p_time)

        s1.fill([0, 0, 0])
        s1.show()

        time.sleep(b_time)

    for n in range(0, 10):
        for d in range(1, 5):
            time_send(d, n)
        time.sleep(1)
        s1.fill([0, 0, 0])
        s1.show()
