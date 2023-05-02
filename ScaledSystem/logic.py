"""
how to create logic
"""

import time

varx = 0

def inc_var():
    global varx
    varx += 1
    print(varx)

class TimeMan:
    def __init__(self, rate:float, do) -> None:
        self.rate = rate
        self.do = do
        self.count = 0
        self.run_t = time.perf_counter()

    def loop(self):
        et = time.perf_counter()-self.run_t
        if self.rate <= et:
            self.do()
            self.run_t = time.perf_counter()

l1 = TimeMan(1, inc_var)

while True:
    l1.loop()
