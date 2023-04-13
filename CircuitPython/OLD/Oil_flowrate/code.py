import board
from digitalio import DigitalInOut, Direction, Pull
from oled import oled_display, oled_text
import countio
import time
import pwmio

# Count rising edges only.
pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE, pull=Pull.DOWN)
# pump_pwm = pwmio.PWMOut(board.GP14, frequency=30, duty_cycle=int(65535 / 2))
flow_k = 23

oled_text("Oil Flowrate")

while True:
    tn = time.monotonic()
    ic = pin_counter.count
    time.sleep(5)
    ac = pin_counter.count
    et = time.monotonic() - tn
    f = (ac - ic) / et
    print(ic, ac)

    flow = f / flow_k
    oled_text(f"LPM: {flow}")

    if pin_counter.count >= 10000:
        pin_counter.reset()
