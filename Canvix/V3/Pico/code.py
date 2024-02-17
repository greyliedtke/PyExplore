"""
main run file 
...globals
"""

import time
import random
from Examples.ClockMan import clock

while True:
    clock.loop()
    time.sleep(.1)