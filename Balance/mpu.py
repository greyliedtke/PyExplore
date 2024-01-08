""" 
reading from mpu6050 with RPI
"""

import smbus
import time      
import math

# initialize bus
bus = smbus.SMBus(1)
MPU6050_ADDRESS = 0x68

bus.write_byte_data(MPU6050_ADDRESS, 0x6B, 0x00)  # Power on
bus.write_byte_data(MPU6050_ADDRESS, 0x1B, 0x08)  # Set full-scale range of the gyroscope to +/- 500 degrees per second
bus.write_byte_data(MPU6050_ADDRESS, 0x1C, 0x08)  # Set full-scale range of the accelerometer to +/- 4g

def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDRESS, reg)
    low = bus.read_byte_data(MPU6050_ADDRESS, reg+1)
    value = (high << 8) + low
    return value

def read_word_2c(reg):
    value = read_word(reg)
    if (value >= 0x8000):
        return -((65535 - value) + 1)
    else:
        return value

def read_acc():
    accel_x = read_word_2c(0x3B)
    accel_y = read_word_2c(0x3D)
    accel_z = read_word_2c(0x3F)
    return [accel_x, accel_y, accel_z]

def read_gyro():
    gyro_x = read_word_2c(0x43)
    gyro_y = read_word_2c(0x45)
    gyro_z = read_word_2c(0x47)
    return [gyro_x, gyro_y, gyro_z]

def read_theta():
    acc = read_acc()
    theta =  -1 * (180 / math.pi) * math.atan2(acc[0], math.sqrt(acc[1]**2 + acc[2]**2))
    return theta
