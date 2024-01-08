"""
Main Run file
"""

import cv2
import numpy as np
from detect_ball import detect_green_ball, video_text
from calcs import calculate_speeds, get_angle

# Main function
def main():
    # Open a video capture object (change the index if needed)
    cap = cv2.VideoCapture(1)

    prev_position = None
    prev_time = cv2.getTickCount()

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read(0)
        if not ret:
            break

        # Detect the green ball in the frame
        ball_position = detect_green_ball(frame)

        # Calculate time elapsed
        curr_time = cv2.getTickCount()
        time_elapsed = (curr_time - prev_time) / cv2.getTickFrequency()

        # Display position and speeds on the frame
        if ball_position:
            x, y = ball_position
            speed_x, speed_y = calculate_speeds(ball_position, prev_position, time_elapsed)
            theta = get_angle(ball_position, ball_position)
            video_text(frame, x, y, speed_x, speed_y, time_elapsed, theta)

        # Display the frame
        cv2.imshow('Video', frame)

        # Update previous position and time
        prev_position = ball_position
        prev_time = curr_time

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
