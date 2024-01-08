"""
calculations
"""
from detect_ball import origin
import math

# Function to calculate ball speeds
def calculate_speeds(curr_position, prev_position, time_elapsed):
    if prev_position is not None:
        dx = curr_position[0] - prev_position[0]
        dy = curr_position[1] - prev_position[1]
        speed_x = dx / time_elapsed
        speed_y = dy / time_elapsed
        return speed_x, speed_y
    return 0, 0

# calculating angle
def get_angle(b1, b2):
    # using two reference postions get angle pendulum is at...
    dx = origin[0] - b1[0]
    dy = origin[1] - b1[1]
    theta = math.atan(dx/dy)
    deg = math.degrees(theta)
    return deg