""" testing acc with rpi"""
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
    

def read_theta():
    accel_x = read_word_2c(0x3B)
    accel_y = read_word_2c(0x3D)
    accel_z = read_word_2c(0x3F)
    theta =  -1 * (180 / 3.14159) * math.atan2(accel_x, math.sqrt(accel_y**2 + accel_z**2))
    gyro_x = read_word_2c(0x43)
    return theta, gyro_x

    
# while True:
#     gyro_x = read_word_2c(0x43)
#     gyro_y = read_word_2c(0x45)
#     gyro_z = read_word_2c(0x47)
#     accel_x = read_word_2c(0x3B)
#     accel_y = read_word_2c(0x3D)
#     accel_z = read_word_2c(0x3F)
#     print("Gyro: ", gyro_x, gyro_y, gyro_z)
#     print("Accel: ", accel_x, accel_y, accel_z)
#     time.sleep(0.1)