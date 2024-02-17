# from CaveMan import cm, game_l
# from PingMan import pm
from ClockMan import clock
from Mat import characters
import time

# game mode
game_mode = "Clock"

# Function to update the scatter plot
def update(frame):
    if game_mode == "Clock":
        clock.loop()
        
while True:
    update()
    time.sleep(1)