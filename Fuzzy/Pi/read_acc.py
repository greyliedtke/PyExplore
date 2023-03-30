""" testing acc with rpi"""
from mpu_6050 import read_theta
from fuzz_control import servo_reponse
import time
from servo import send_servo_angle

prev_theta = 0

def theta_filter(current, prev):
    current = prev*.1+current*.9
    return prev, current

while True:
    theta = read_theta()
    prev_theta, theta = theta_filter(theta, prev_theta)
    send_serv = servo_reponse(theta)
    send_servo_angle(send_serv)
    print(theta, send_serv)
    time.sleep(0.5)
