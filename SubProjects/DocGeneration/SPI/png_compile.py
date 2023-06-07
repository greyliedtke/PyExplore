"""
Script to turn a bunch of pngs into a single pdf
"""

from fpdf import FPDF
import os


pdf = FPDF()
pdf.set_auto_page_break(0)

img_f_path = '../SCG/SCG_Processing/Figures/scg_07_figs'
images = os.listdir(img_f_path)

for f in images:
    pdf.add_page()
    pdf.image(img_f_path+'/'+f)

pdf.output('SCG_07Figs.pdf')


# create figure
# def fig_dir():
#     # function to plot every column and save figure of dataframe
#     # create directory
#     os.mkdir(dir_path+test)
#     # plot every column vs. runtime...
#     for c in df.columns:
#         try:
#             plot_man(df, 'ni_elapsed_sec', y_data=[c], save=dir_path+test+'/'+c, grid=True, x_label='Elapsed Sec')
#         except:
#             print(f'Cant plot: {c}')