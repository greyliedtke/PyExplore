
import matplotlib.pyplot as plt
# %matplotlib widget
# https://matplotlib.org/stable/plot_types/basic/index.html

fig, ax = plt.subplots()
ax.bar(counts.index, counts.values)
ax.tick_params(rotation=45)
plt.show()


# create correlation matrix
corr_matrix = df.corr()

# Create the heatmap
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()

# Add xticks and yticks
plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix)), corr_matrix.columns)

# Show the plot
plt.show()


def plot_man(df, x_data, y_data, y_2data=(), sub_y=(), legend=False, title=None, x_label=None, y_label=None,
             x_lim=None, y_lim=None, y_2lim=None, sub_y_label=None,
             grid=False, save=None, show=False):
    fig, ax = plt.subplots()

    def y_plots(axd, xd, yd):
        for y_p in sub_y:
            axd.plot(df[xd], df[yd])

    # loop through y plots
    y_plots(ax, x_data, y_data)
    ax.legend(y_data)

    # subplots
    if len(sub_y) > 0:
        fig, (ax, ax_2) = plt.subplots(2, 1)
        y_plots(ax2, x_data, sub_y)
        ax_2.set_ylabel(sub_y_label)

    # second axis plotting...
    if len(y_2data) > 0:
        ax2 = ax.twinx()
        y_plots(ax2, x_data, sub_y)

    # formatting
    if x_lim is not None:
        ax.set_xlim(x_lim)
    if y_lim is not None:
        ax.set_ylim(y_lim)
    if title is not None:
        ax.set_title(title)
    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)
    if grid is True:
        ax.grid()
    if save is not None:
        fig.savefig(save+'.png')