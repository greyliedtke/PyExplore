"""
script to create matplotlib figures
"""

import matplotlib.pyplot as plt
import pandas as pd

# Create matplotlib figures
def pf(
    df: pd.DataFrame,
    y_cols: list,
    x_col="elapsed_sec",
    x_title="Elapsed Seconds",
    y_title="",
    title="",
    folder="test",
    x_lim=None,
    y_lim=None,
):
    plt.close()
    # fig_spr = pf(df_results, "Compressor.RVD.RR", ["Compressor.RVD.SPR"], "RR", "SPR", x_lim=[1,2], title="SPR", folder=fstudy)
    fig, ax = plt.subplots()
    for i, y in enumerate(y_cols):
        ax.plot(df[x_col], df[y])

    if y_lim != [0,0]:
        ax.set_ylim(y_lim)
    if x_lim != [0, 0]:
        ax.set_xlim(x_lim)

    ax.legend(y_cols)
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.grid()
    plt.close()

    return fig