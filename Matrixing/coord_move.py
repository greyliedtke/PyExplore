# MOVIE

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import math

fig, ax = plt.subplots(1, 1)

t = np.linspace(0,16)
x = np.linspace(-8,8)
y = 2*t - 1*x

df = pd.DataFrame({"time": t, "x":x, "y":y})
df["y"] = 1*df["x"].apply(np.sin)
df["y2"] = -1*df["x"].apply(np.sin)

# # Loop to show a new plot every interval
while True:
    for i, row in df.iterrows():

        pdf = df[:i]

        ax.clear()  # Clear the plot
        ax.set_ylim([-2,2])
        ax.set_xlim([-8,8])

        ax.plot(pdf["x"], pdf["y"])  # Plot the data
        ax.plot(pdf["x"], pdf["y2"])  # Plot the data
        plt.pause(0.05)  # Pause to display the plot for 0.1 seconds

# Display the final plot

plt.show()