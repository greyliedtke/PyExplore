import numpy as np
import time

# Define a 16x16 matrix to represent the clock display
clock_display = np.zeros((16, 16), dtype=int)

while True:
    # Get the current time
    current_time = time.strftime("%H:%M:%S")
    
    # Clear the clock display
    clock_display.fill(0)
    
    # Convert the current time to a binary string
    binary_time = "".join(format(int(x), "04b") for x in current_time.replace(":", ""))
    
    # Update the clock display with the binary time
    for i in range(16):
        for j in range(16):
            index = i * 16 + j
            if index < len(binary_time):
                clock_display[i][j] = int(binary_time[index])

    # Display the clock
    for row in clock_display:
        print("".join(['#' if x == 1 else ' ' for x in row]))
    
    # Wait for 1 second
    time.sleep(1)
