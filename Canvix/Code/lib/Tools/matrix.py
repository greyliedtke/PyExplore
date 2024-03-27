"""
file to represent matrix
use adafruit matrix library...
1. Send pixels 
2. Draw lines
3. Send characters
4. bounding box for thickness
"""

class Matrix:
    length = 16

    def send_point(x, y, color):
        print(f"sent point at {x}, {y} with color {color}")

if __name__ == "__main__":
    print(Matrix.length)