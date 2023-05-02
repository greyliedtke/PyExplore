"""
creating script to simulate automated testing
- follow load paths
- schedule shutdowns
- variable limits and shutdowns
- sensor discrepancy
"""

import numpy as np
import pandas as pd

# function to find errors large descrepancies and return average of readings
def sensor_discrep(readings: dict):
    sensor_readings = list(readings.values())
    avg = np.average(sensor_readings)
    std_dev = np.std(sensor_readings)
    print(f"stdev: {std_dev}, avg: {avg}")
    good_readings = {}
    for k, v in readings.items():
        dev = abs(avg-v)
        if dev > 1.5*std_dev:
            print(f"suspect: {k}")
        else:
            good_readings[k] = v
    sensor_avg = np.average(list(good_readings.values()))
    return sensor_avg






