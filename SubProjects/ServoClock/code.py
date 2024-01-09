# imports
from servos import send_servo_digits
import time

# ------------------------------------------------------
for d in range(0,10):
    send_servo_digits(d)
    time.sleep(1)
