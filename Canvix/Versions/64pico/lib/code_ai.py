# imports
import board
import pwmio
import time
import analogio
from ulab import numpy as np
from ulab.scipy.signal import spectrogram

ai_acc = analogio.AnalogIn(board.A0)  # fuel analog input


# pwm signal to transitor for speed simulation
servo_pwm = pwmio.PWMOut(board.GP0, frequency=50, duty_cycle=0)

def send_servo_angle(theta):
    duty_percent = theta*(100/180)
    duty_percent = (2.5+duty_percent/10)/100
    cycle = int(duty_percent*65535)
    print(duty_percent)
    # Cycles through the full PWM range from 0 to 65535
    servo_pwm.duty_cycle = cycle  # Cycles the LED pin duty cycle through the range of values
    # pi.set_PWM_frequency(servo_pin, freq)


def speed_test():
    samples = 1024
    d = []
    ts = time.monotonic_ns()
    for i in range(samples):
        d.append(ai_acc.value)

    s = (time.monotonic_ns()-ts)*1e-9
    # ta = np.linspace(0, samples, num=samples)
    # ffa = np.fft.fft(data)
    print(d)
    hz = samples/s
    # print(hz, "hz")
    # print(max(d), "time_ms: ", s)

while True:
    speed_test()
    print()
    time.sleep(1)

s_time = .05
cmds = [0,180]

while True:
    for c in cmds:
        send_servo_angle(c)
        time.sleep(s_time)
