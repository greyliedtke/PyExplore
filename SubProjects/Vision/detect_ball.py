"""
detect ball
"""

import cv2
import numpy as np

origin = (300,150)

# info box
def video_text(frame, x, y, speed_x, speed_y, time_elapsed, degrees):
    cv2.circle(frame, (origin[0], origin[1]), 10, (255, 0, 0), -1)
    cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
    cv2.putText(frame, f'Position: ({x}, {y})', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Speeds: ({speed_x:.2f}, {speed_y:.2f})', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'dt: {time_elapsed}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'angle: {degrees}', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Function to detect the green ball in a frame
def detect_green_ball(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for the green ball
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # Create a mask for the green ball
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contour is found
    if contours:
        # Get the largest contour (assumed to be the green ball)
        green_ball_contour = max(contours, key=cv2.contourArea)

        # Get the coordinates of the green ball
        x, y, w, h = cv2.boundingRect(green_ball_contour)
        return x, y

    return None