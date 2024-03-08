"""
script for plotting many things...
"""
import matplotlib.pyplot as plt
from sklearn import linear_model

# Genertic creating figure for multiple columns
def pf(df, x_col, y_cols, x_title="", y_title="", title="", x_lim=None, y_lim=None, save=None):
    # fig_spr = pf(df_results, "Compressor.RVD.RR", ["Compressor.RVD.SPR"], "RR", "SPR", x_lim=[1,2], title="SPR", folder=fstudy)
    fig, ax = plt.subplots()
    for y in y_cols:
        ax.plot(df[x_col], df[y])

    if y_lim != 0:
        print(y_lim)
        ax.set_ylim(eval(y_lim))
    if x_lim != [0, 0]:
        ax.set_xlim(x_lim)

    ax.legend(y_cols)
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.grid()
    if save:
        fig.savefig(save)
    return fig