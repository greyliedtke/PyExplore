"""
main run file 
...globals
"""

# Libraries ------------------------------------------------
import time
import Tools.Matrix as matrix
from Tools.Hardware import encoder_left, encoder_right, led_strip
from Tools.Colors import colors
from Examples.Clock import clock_mode
from Examples.Bouncer import bouncer
# -------------------------------------------------

# Coding -------------------------------------------------
loop_speed = 1 # This is a variable. The loop will run every 1 second
MODE = []
# -------------------------------------------------

# -------------------------------------------------
while True: # This is a loop that will run forever

    # changing mode if both buttons are pressed -------
    encoder_left.read()
    encoder_right.read()
    if encoder_left.held() and encoder_right.held():
        MODE = (MODE + 1) % 3
    # -------------------------------------------------

    # -------------------------------------------------
    # print("Hello") # Print hello every second
    # time.sleep(loop_speed) # This will pause the code for 1 second
    # -------------------------------------------------

    # -------------------------------------------------
    if MODE == 0: # Art loop
        for color in colors: # This is a loop that will run 3 times
            led_strip.set_color(colors)
            time.sleep(loop_speed) # This will pause the code for 1 second
    elif MODE == 1: # Clock display
        clock_mode.loop()
    elif MODE == 2: # ball bouncing
        bouncer.loop()

    # -------------------------------------------------

# -------------------------------------------------
# LED Controls
#LEDStrip.set_color('red')
#LEDStrip.set_pixel(100, 'green')
#LEDStrip.set_matrix([4,8] 'blue')
# cycle_colors()
# -------------------------------------------------
