"""
main run file 
...globals
"""
import microcontroller
print(microcontroller.cpu.temperature)
print('temp')


import time
import random
from Examples.ClockMan import clock
from Examples.ColorFade import colorfade
# from Examples.CaveMan import cm

print("running loop")

while True:
    clock.loop()
    # cm.loop()
    # colorfade.loop()
    # colorfade.loop()
    # time.sleep(.01)
