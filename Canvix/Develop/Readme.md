
### Ideas

- creating intro lesson for new users
   
1. Driving LEDS
  1. set all pixels to color
  2. Set pixel to color
  3. set array of pixels to colors
2. Equations
  1. y = mx+b
  2. y = sin(x)
3. Animations
4. Sensors
5. Games


### Code.py


#### Initializing everything
- imports
  - Tools
    - Hardware
      - LED strip
        - 1 long strip of lights
        - All have three lights...
          - Red, Green, Blue
          - Using these three colors, we can make any color
      - Rotary encoders
        - detect rotation
        - detect button press
        - detect button hold
    - Matrix
      - Creating characters from pixels
      - Turning matrix into x,y coordinates
    - Colors
      - RGB 
    - Math
      - Turning equations into pixels
      - Interpolating lines
      - Creating bounding boxes
    - Time
- Examples
  - Pages
    - Art
      - Golden Gate bridge
      - Flowers
      - Make your own!
    - Tetris
    - Pong
    - CaveRunner
    - Sine wave
    - Bouncing ball
    - Sparkling Colors 
    - RGB

### Learn to code 
- variables
- loops
- if statements
- functions
- libraries
  - time
  - board
  - neopixel
  - rotaryio

### Code.py

'''
import time
'''

### Code.py

```python
# -------------------------------------------------
# importing libraries to use
import time
import Tools.Hardware.LEDStrip as LEDStrip
# -------------------------------------------------

# -------------------------------------------------
# Coding
# '#': is a comment. This line is ignored by the computer
loop_speed = 1 # This is a variable. The loop will run every 1 second
MODE = []
def cycle_colors():
  for color in ['red', 'green', 'blue']: # This is a loop that will run 3 times
    LEDStrip.set_color(colors)
    time.sleep(loop_speed) # This will pause the code for 1 second
# -------------------------------------------------

# -------------------------------------------------
while True: # This is a loop that will run forever

  # -------------------------------------------------
  # print("Hello") # Print hello every second
  # time.sleep(loop_speed) # This will pause the code for 1 second
  # -------------------------------------------------

  # -------------------------------------------------
  if MODE == 0: # Art loop
  elif MODE == 1: # Clock display
  elif MODE == 2: # Game
  elif MODE == 3: # Animation
  elif MODE == 4: # LED Controls

  # -------------------------------------------------

  # -------------------------------------------------
  # LED Controls
  #LEDStrip.set_color('red')
  #LEDStrip.set_pixel(100, 'green')
  #LEDStrip.set_matrix([4,8] 'blue')
  # cycle_colors()
  # -------------------------------------------------


```


