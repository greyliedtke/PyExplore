"""
master script for creating commonly used ploting tools
"""

import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib widget

# ------------------------------------------------------
def simple_plot(df):
    # simple plot figure
    fig, ax = plt.subplots()
    ax.plot(df["example"], df["example"])
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.legend(["example", "example"])
    ax.set_title("title")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.grid()
    plt.show()
# ------------------------------------------------------


# ------------------------------------------------------
# Genertic creating figure for multiple columns
def pf(df, x_col, y_cols, x_title="", y_title="", title="", x_lim=None, y_lim=None):
    # fig_spr = pf(df_results, "Compressor.RVD.RR", ["Compressor.RVD.SPR"], "RR", "SPR", x_lim=[1,2], title="SPR", folder=fstudy)
    fig, ax = plt.subplots()
    for y in y_cols:
        ax.plot(df[x_col], df[y])

    if y_lim != [0, 0]:
        ax.set_ylim(y_lim)
    if x_lim != [0, 0]:
        ax.set_xlim(x_lim)

    ax.legend(y_cols)
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.grid()
    return fig
# ------------------------------------------------------

# ------------------------------------------------------
# Plotting multiple subplots
def plot_comp(df, cols, x):
    fig, axs = plt.subplots(len(cols), 1)
    for i, col in enumerate(cols):
        if type(col) == list:
            for c in col:
                axs[i].plot(df[x], df[c])
            axs[i].legend(col)
        else:
            axs[i].plot(df[x], df[col])
            axs[i].set_ylabel(col, rotation=0, labelpad=60)

        axs[i].grid()
        if i == len(cols) - 1:
            axs[i].set_xlabel("Time (s)")
        else:
            axs[i].set_xticklabels([])
    return fig
# ------------------------------------------------------

# ------------------------------------------------------
# Plotting across axis
def plot_2y(df, x_col, y1c, y2c):
    fig, axl = plt.subplots(1, 1)
    axl.plot(df[x_col], df[y1c], label=y1c)
    axr = axl.twinx()
    for c in y2c:
        axr.plot(df[x_col], df[c], label=c, linestyle="--")
    axl.legend(loc="upper left")
    axr.legend(loc="upper right")
    return fig
# ------------------------------------------------------