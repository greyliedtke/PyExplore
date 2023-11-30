"""
Script to simplify manipulating of csv files
"""

# imports
import matplotlib.pyplot as plt
import pandas as pd


class CSVMan:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def show_columns(self):
        # get all columns from dataset
        print(self.df.columns)

    def scatter_plot(self, x_column, y_columns, y2_columns=None, title=None, legend=None, x_label=None, y_labels=None):
        # initialize figure with subplots
        fig, ax1 = plt.subplots()

        # initialize arrays to plot
        x_array = self.df[x_column]
        y_arrays = []

        # if multiple y columns to plot
        if len(y_columns) > 1:
            for col in y_columns:
                y_arrays.append(self.df[col])
            legend = "Default"
            y_label = y_columns

        # if single y column plotting
        else:
            y_label = y_columns
            y_arrays = [self.df[y_columns]]

        # adding onto first y axis
        for y in range(len(y_arrays)):
            ax1.plot(x_array, y_arrays[y], label=y_columns[y])

        # formatting things
        ax1.set_xlabel(x_column)
        ax1.set_ylabel(y_label)
        ax1.set_title(title)

        """
        Figure out for 2 y axis...
        ax2 = ax1.twinx()
        ax2.plot(range(len(df[fp])), df[n2], '-r')
        ax2.set_ylabel(n2)
        ax2.legend([n2])
        """

        # showing legend
        if legend == "Default":
            ax1.legend()

        # showing plot
        plt.show()


"""
Example code

test = CSVMan("plc_chopped.csv")
test.show_columns()
test.scatter_plot('Index', ['n2 speed sensor', 'Power [kW]'])

"""

# END
