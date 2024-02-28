
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
    - Colors 
    - Math
    - Time
  - Examples
    - Art
      - For a in art:
      - Art
      - Golden Gate bridge
      - Flowers
      - Make your own!
    - Games
      - Tetris
      - Snake
      - Pong
      - CaveRunner
    - Clock
    - Animations
      - Sine wave
      - Bouncing ball - change velocity
      - Sparkling stars
      - rgb colors
      - juggling

    - Pages
    - Art
    - 
  

- while loop
  - if statements
  - logic
  - delay
- - Import necessary modules:
    - `datetime` module for handling dates and times.
    - `pf` and `plot_comparison` functions from `Tools.plot`.
    - `fft_krpm` and `get_rms` functions from `Tools.acc_processing`.
    
- Define function `am_test(t_id)`:

    ```python
    def am_test(t_id):
    ```

- Read accelerometer data from CSV file:
    
    ```python
    df_acc = pd.read_csv(
        f"Lib/2402_AirSpinTesting/Processing/RunFiles/Good_Data/{t_id}/acc_raw.csv"
    )
    ```

- Read speed data from CSV file:
    
    ```python
    df_speed = pd.read_csv(
        f"Lib/2402_AirSpinTesting/Processing/RunFiles/Good_Data/{t_id}/speeds_p.csv"
    )
    ```

