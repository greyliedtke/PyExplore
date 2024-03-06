"""
script to analyze T07 data
- calculations
- figures
- cycle deck
"""

# imports
# ------------------------------------------------------
import pandas as pd
import os
from Tools.calcs import calcs_t07
from Tools.matplot_figure import pf
import os, sys
from Tools.plots import plots
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# ------------------------------------------------------

# ------------------------------------------------------
# select run file
rf = "Data/231027_01.csv"
rf = "Data/230210_02.csv"
rf = "Data/230405_02.csv"

df = pd.read_csv(rf)
test_name = os.path.basename(rf).split('.')[0]
path_folder = f"Processed/{test_name}"
if not os.path.exists(path_folder):
    os.makedirs(path_folder)
if not os.path.exists(path_folder+"/figs"):
    os.makedirs(path_folder+"/figs")
dfc = list(df.columns)
# ------------------------------------------------------

# ------------------------------------------------------
# plots and calculations for config
df = df.query("CV_PLC_Stage>10")
df = calcs_t07(df)  
df.to_csv(f"{path_folder}/data.csv")
# ------------------------------------------------------

# ------------------------------------------------------
# STANDARD PLOTS
for k,v in plots.items():
    try:
        fig = pf(df, v["Cols"], x_col="elapsed_sec", title=k, y_title=v["Units"], y_lim=v.get("Limits", 0))
        fig.savefig(f"{path_folder}/figs/{k}.png")
    except Exception as e:
        print(f"ERROR: {e}")
# ------------------------------------------------------
