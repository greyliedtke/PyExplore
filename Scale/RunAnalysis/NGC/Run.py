"""
script to analyze T07 data
- calculations
- figures
- cycle deck
"""

# imports
# ---------------------------------------------f---------
import pandas as pd
import os
import plots
import os, sys
import calcs
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# ------------------------------------------------------

# ------------------------------------------------------
# select run file
rf = "Data/12k_7s.csv"   # 7 second ramp
rf = "Data/whole.csv"   # big data


df = pd.read_csv(rf)
test_name = os.path.basename(rf).split('.')[0]
path_folder = f"Processed/{test_name}"
if not os.path.exists(path_folder):
    os.makedirs(path_folder)
if not os.path.exists(path_folder+"/figs"):
    os.makedirs(path_folder+"/figs")
dfc = list(df.columns)
with open(f"{path_folder}/columns.py", 'w') as file:
        file.write("columns" + " = [\n")
        for row in dfc:
            file.write(f"['{row}'],\n")
        file.write("]\n")

# ------------------------------------------------------

# ------------------------------------------------------
# plots and calculations for config
df = df.query("cc_pr>1.6")

# df = calcs.calcs_t05(df)
# performing calculations on datas

df.to_csv(f"{path_folder}/data.csv")
# ------------------------------------------------------
plots.create_trend(df, "cc_pr", "cv_dc_kw", "PR vs Power", "PR", "Power", save=f"{path_folder}")
plots.create_trend(df, "cc_pr", "cc_n2", "PR vs N2", "PR", "kRPM", save=f"{path_folder}")

# ------------------------------------------------------
# STANDARD PLOTS to loop through
for k,v in plots.plot_dict.items():
    try:
        fig = plots.pf(df, x_col="elapsed_sec", y_cols=v["Cols"], title=k, y_title=v.get("Units"), y_lim=v.get("Limits", 0), save=path_folder)
    except Exception as e:
        print(f"ERROR: {e}")
# ------------------------------------------------------
