# sudo chmod a+rw /dev/ttyACM0

# neopixel strip

# turn all on color
print("hey grey")

import neopixel
import board
import time
import random

# INITIALIZE PIXELS
s1_len = 60
s1 = neopixel.NeoPixel(board.GP0, s1_len, auto_write=False)

# COLORS
d_colors = {"red": [9, 4, 1], "blue": [1, 4, 9]}

s1.fill(d_colors["red"])
s1.show()

cc = "blue"




fill_range = range(16, 60)
l1 = list(reversed(list(range(3, 18))))
l2 = list(reversed(list(range(18, 45))))
clock_a = l1+l2






mins = 0

while True:

    # for f in clock_a:
    #     s1[f] = d_colors[cc]
    #     s1.show()
    #     time.sleep(1.46)

    l1 = list(reversed(list(range(3, 18))))
    l2 = list(reversed(list(range(18, 45))))
    clock_a = l1+l2
        
    # mya = clock_a

    for p in range(len(clock_a)):
        # random_index = random.randint(0, len(mya) - 1)
        # Remove the element at the random index
        # removed_value = mya.pop(random_index)

        # s1[removed_value] = d_colors[cc]
        print(clock_a[p])
        s1[clock_a[p]] = d_colors[cc]
        s1.show()
        time.sleep(.1)

    # mya = clock_a

    if cc == "red": cc="blue"
    else: cc = "red"

    mins+=1
    print(mins)
    
