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
import Tools.plots as plots
import os, sys
from scipy.signal import savgol_filter
import Tools.calcs as calcs
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# ------------------------------------------------------

# ------------------------------------------------------
# select run file
rd = {
    "12kRamp": {"file": "Data/12k_20s.csv"},
}

rk = "12kRamp"
rf = rd[rk]["file"]
df = pd.read_csv(rf)
avg_time = rd[rk].get("avg_time", False)
if not avg_time:
    avg_time = [min(df['elapsed_sec']), max(df['elapsed_sec'])]

test_name = os.path.basename(rf).split(".")[0]
test_name = rk
path_folder = f"Out/{test_name}"
if not os.path.exists(path_folder):
    os.makedirs(path_folder)
if not os.path.exists(path_folder + "/figs"):
    os.makedirs(path_folder + "/figs")
dfc = list(df.columns)
with open(f"{path_folder}/columns.py", "w") as file:
    file.write("columns" + " = [\n")
    for row in dfc:
        file.write(f"['{row}'],\n")
    file.write("]\n")
# ------------------------------------------------------

# ------------------------------------------------------
# plots and calculations for config
df = df.query("CV_PLC_Stage>10")

# power
df["Power"] = df["cv_dc_kw"]

# fuel
rho_fuel = 0.817  # kg/m^3
hhv = 43e3  # MJ/kg
df["fuel_kgs"] = df["PLC_VF_Fuel"] * rho_fuel / 60
df["fuel_energy"] = df["fuel_kgs"] * hhv
df["fuel_eff"] = 100 * (df["Power"] / df["fuel_energy"])

# ------------------------------------------------------
# Pressures
pt_exit_cols = ["PLC_PT_Exit_Flow_1", "PLC_PT_Exit_Flow_2", "PLC_PT_Exit_Flow_3", "PLC_PT_Exit_Flow_4"]
df["P_PT_Exit"] = df[pt_exit_cols].mean(axis=1)
df["PR"] = df["cc_pr"]
df["speed_ratio"] = df["PLC_N_N2a"] / df["PLC_N_N1a"]
# ------------------------------------------------------

# ------------------------------------------------------
# Compressor Efficiency
df["T_Inlet"] = df[["NI_T_Ambient"]].mean(axis=1)
t_pt_exit_cols = [
    "PLC_T_PT_Exit_Flow_1",
    "PLC_T_PT_Exit_Flow_2",
]
df["T_PT_Exit"] = df[t_pt_exit_cols].mean(axis=1)
t_rc = (df["T_PT_Exit"] + 273.15) / (df["T_Inlet"] + 273.15)
df["comp_eff_pt"] = ((df["PR"] ** (0.4 / 1.4) - 1) / (t_rc - 1)) * 100
# ------------------------------------------------------

# ------------------------------------------------------
# Leakage
t_pt_ducts = [
    "PLC_T_Cross_Duct_Flow_2",
]
df["T_PT_Duct"] = df[t_pt_ducts].mean(axis=1)
df["T_Bypass"] = df[
    ["PLC_T_Seal_Bypass_Flow_1", "PLC_T_Seal_Bypass_Flow_2"]
].mean(axis=1)
df["leakage"] = (
    (df["T_PT_Duct"] - df["T_PT_Exit"]) / (df["T_Bypass"] - df["T_PT_Exit"])
) * 100
df["leakage_smooth"] = savgol_filter(df["leakage"], 20, 3)
# ------------------------------------------------------

# ------------------------------------------------------
# Loop through cycle deck and make plots
v_avgs = {}
df_cd = pd.read_excel("cycle_deck.xlsx")
md_string = f"#  {test_name} Cycle Deck\n\n"
md_string += "\n"

for i, r in df_cd.iterrows():
    try:
        plots.pf(
            df,
            x_col="elapsed_sec",
            y_cols=eval(r["Columns"]),
            title=r["Title"],
            x_title="Time [s]",
            y_title=r["Units"],
            y_lim=r["ylim"],
            save=f"{path_folder}/figs/{r['Title']}.png",
        )
        avg_v = df.query(f"elapsed_sec>{avg_time[0]} & elapsed_sec<{avg_time[1]}")[
            eval(r["Columns"])
        ].mean()
        avg_v = avg_v.values[0]
        v_avgs[r["Title"]] = {"Avg": avg_v, "Units": r["Units"]}
        md_string += f"{r['Title']}![png](figs/{r['Title']}.png)\n\n"
    except Exception as e:
        print(f"Error:{e}")

df_avgs = pd.DataFrame(v_avgs).T.reset_index()
df_avgs.columns = ["Title", "Avg", "Units"]
df_avgs.to_csv(f"{path_folder}/avgs.csv")
md_string += f"\n\n Averages over period: {avg_time[0]} to {avg_time[1]}s\n\n"
md_string += df_avgs.to_markdown()
with open(f"{path_folder}/{rk}.md", "w") as f:
    f.write(md_string)
# ------------------------------------------------------
