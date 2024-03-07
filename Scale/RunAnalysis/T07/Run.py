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
import plots
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# ------------------------------------------------------

# ------------------------------------------------------
# select run file
rf = "Data/231027_01.csv"
rf = "Data/230210_02.csv"
# rf = "Data/230405_02.csv"

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

import Calcs.power as power
df = power.power(df)
# performing calculations on datas

df.to_csv(f"{path_folder}/data.csv")
# ------------------------------------------------------

plots.pf(df, x_col="PR", y_cols=["kw_4wi"], title="PR vs PWR", y_title="kW", save=f"{path_folder}")
plots.pf(df, x_col="PR", y_cols=["N_PLC_N2"], title="PR vs N2", y_title="kRPM", save=f"{path_folder}")
# plots.pf(df, x_col="PR", y_cols=["MF_Bellmouth"], title="PR vs MF", y_title="kg/s", save=f"{path_folder}")
plots.create_trend(df, "PR", "Power", "PR vs PWR", "PR", "kW", save=f"{path_folder}")

# ------------------------------------------------------
# STANDARD PLOTS to loop through
for k,v in plots.plot_dict.items():
    try:
        fig = plots.pf(df, x_col="elapsed_sec", y_cols=v["Cols"], title=k, y_title=v.get("Units"), y_lim=v.get("Limits", 0), save=path_folder)
    except Exception as e:
        print(f"ERROR: {e}")
# ------------------------------------------------------
