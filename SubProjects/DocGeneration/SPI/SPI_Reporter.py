# import necessary libraries and connect to database

import pandas as pd
from scipy.signal import savgol_filter
import os

# create directory
script_dir = "ScaledWiki/DataServer/SPI_Data_Report/"
test_name = input("test_name: ")
test_directory = script_dir + "TestReports/" + test_name

if not os.path.exists(test_directory):
    os.makedirs(test_directory)
    os.makedirs(test_directory+'/Figs')
    print(f"Created directory: {test_directory}")
else:
    print(f"Directory already exists: {test_directory}")

# plotting generator
from Scripts.FigureGenerator import dp_plot
from Scripts.Calcs import TestDataset

# Calculations ----------------------------------------------------------------
df = pd.read_csv(script_dir+"Data/1_24_20kw.csv")
dataset = TestDataset(df, test_name)
dataset.run_resizer()
df = dataset.run_calcs()


# Create Figures ----------------------------------------------------------------
plot_df = pd.read_excel(script_dir + "TemplateFiles/SPI_PlottingBook_r.xlsx")
plot_groups = list(plot_df["Group"].unique())
imgs = []

for i, row in plot_df.iterrows():
        try:
            png = dp_plot(
                df,
                row["x"],
                eval(row["y"]),
                row["x_label"],
                row["y_label"],
                row["title"],
                exp_r=row["Expected_range"],
                directory=test_directory+'/Figs/'
            )
            if png != "NA":
                imgs.append(png)
        except:
            print(f'failed to create: {row["title"]}')


# Create PDF ----------------------------------------------------------------
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font()
pdf.set_font("Helvetica", "", 14)
pdf.write(5, 'Name: '+dataset.test_name + "\n")
pdf.write(5, 'Description: '+dataset.description + "\n")
pdf.write(5, 'Runtime (M): '+dataset.runtime + "\n")
pdf.write(5, 'Max Power (kW): '+dataset.max_power + "\n")
pdf.add_page()

for image in imgs:
    pdf.image(image, w=160, h=120)

pdf.output(f"{test_directory}/{test_name}.pdf", "F")
df.to_csv(f"{test_directory}/{test_name}.csv")