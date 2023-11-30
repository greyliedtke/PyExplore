

import matplotlib.pyplot as plt
from pytimedinput import *
from simple_pid import PID  # pid loop for n2

# 
fig, ax = plt.subplots()
y_o = 10
y = [y_o]
x = [0] # time in seconds
lt = .25



def speed_response(fuel_percent, load_level):
    n2_max_sim = 60
    n2_speed = n2_max_sim * fuel_percent / ((1+load_level)/10)
    n1_speed = n2_speed * 1.8
    return round(n1_speed, 1), round(n2_speed, 1)


def pid_loop(n2_val, n2_sp):
    new_output = round(n2_pid(n2_val), 1)
    return new_output
    # execute pid loop and return new fuel output

# on new parameters...


# control parameters
load_level = 1 # out of 12

fuel_ao = init_ao


# create running loop
while True:


    userNumber, timedOut = timedFloat("Enter a floating-point value: ", lt)
    if(not timedOut):
        y_o = userNumber
        print(userNumber)

    y.append(y_o)
    x.append(x[-1]+lt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([x[-1]-20, x[-1]])
    plt.pause(.01)

