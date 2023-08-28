import keyboard
import time

def main_function():
    while not keyboard.is_pressed('q'):  # Change 'q' to the desired key
        # Your function logic here
        print("Function is running...")
        time.sleep(.5)
    timeq = input("Do this now:")
    print(timeq)

if __name__ == "__main__":
    print("Press 'q' to stop the function.")
    main_function()