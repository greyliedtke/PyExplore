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
    "20kw_Recuperated": {"file": "Data/230405_02.csv", "avg_time": [181, 195]},
    "30_kW": {"file": "Data/230210_02.csv", "avg_time": [250, 275]},
    "20kw_Recup_Rect": {"file": "Data/231027_01.csv", "avg_time": [260, 275]},
}

rk = "20kw_Recup_Rect"
rf = rd[rk]["file"]
avg_time = rd[rk]["avg_time"]
df = pd.read_csv(rf)

test_name = os.path.basename(rf).split(".")[0]
test_name = rk
path_folder = f"Out/CD/{test_name}"
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

# massflow
df = calcs.massflow(df)

if rk == "20kw_Recup_Rect":
    df["current"] = df[["I_PLC_Phase_1", "I_PLC_Phase_2", "I_PLC_Phase_3"]].sum(axis=1)
    df["Power"] = df["current"]*120/1000
    df["Power"] = df["Power"] - df["Power"].iloc[0]
    df["N2"] = df["N_PLC_N2"]

# fuel
rho_fuel = 0.817  # kg/m^3
hhv = 43e3  # MJ/kg
df["fuel_kgs"] = df["VF_PLC_Fuel"] * rho_fuel / 60
df["fuel_energy"] = df["fuel_kgs"] * hhv
df["fuel_eff"] = 100 * (df["Power"] / df["fuel_energy"])

# ------------------------------------------------------
# Pressures
pt_exit_cols = ["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"]
df["P_PT_Exit"] = df[pt_exit_cols].mean(axis=1)
df["PR"] = (df["P_PT_Exit"] + 101.325) / 101.325
df["speed_ratio"] = df["N_PLC_N2"] / df["ACC_NI_CH1_FFT"]
# ------------------------------------------------------

# ------------------------------------------------------
# Compressor Efficiency
df["T_Inlet"] = df[["T_PLC_Inlet_1", "T_NI_Inlet_2"]].mean(axis=1)
t_pt_exit_cols = [
    "T_NI_PT_Exit_1",
    "T_NI_PT_Exit_2",
    "T_NI_PT_Exit_3",
    "T_NI_PT_Exit_4",
]
df["T_PT_Exit"] = df[t_pt_exit_cols].mean(axis=1)
t_rc = (df["T_PT_Exit"] + 273.15) / (df["T_Inlet"] + 273.15)
df["comp_eff_pt"] = ((df["PR"] ** (0.4 / 1.4) - 1) / (t_rc - 1)) * 100
# ------------------------------------------------------

# ------------------------------------------------------
# Easier Calcs
df["P_Comb"] = (101.325 + df["P_NI_Combustor_Can_1"]) / (101.325 + df["P_PT_Exit"])

# ------------------------------------------------------
# Leakage
t_pt_ducts = [
    "T_PLC_PT_Outlet_Duct_1",
    "T_PLC_PT_Outlet_Duct_2",
    "T_NI_PT_Outlet_Duct_3",
    "T_NI_PT_Outlet_Duct_5",
    "T_NI_PT_Outlet_Duct_6",
    "T_NI_PT_Outlet_Duct_7",
]
t_bypass = ["T_NI_Seal_Bypass_1", "T_NI_Seal_Bypass_3", "T_NI_Seal_Bypass_4"]
df["T_PT_Duct"] = df[t_pt_ducts].mean(axis=1)
df["T_Bypass"] = df[t_bypass].mean(axis=1)
df["leakage"] = (
    (df["T_PT_Duct"] - df["T_PT_Exit"]) / (df["T_Bypass"] - df["T_PT_Exit"])
) * 100
df["leakage_smooth"] = savgol_filter(df["leakage"], 20, 3)

# validation plots
plots.pf(
            df,
            x_col="elapsed_sec",
            y_cols=t_pt_ducts+t_bypass+t_pt_exit_cols,
            title="T PT Ducts and Bypass",
            x_title="Time [s]",
            y_title="C",
            save=f"{path_folder}/figs/T PT Ducts.png",
        )
# ------------------------------------------------------

# recuperator averaging
if "T_PLC_Recuperator_HP_Outlet_1" in df.columns:
    df = calcs.recuperator_efficiency(df)

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
        md_string += f"## {r['Title']}\n![png](figs/{r['Title']}.png)\n\n"
    except Exception as e:
        print(f"Error:{e}")

df_avgs = pd.DataFrame(v_avgs).T.reset_index()
df_avgs.columns = ["Title", "Avg", "Units"]
df_avgs.to_csv(f"{path_folder}/avgs.csv")
md_string += f"## Summary Table"
md_string += f"\n\n Averages over period: {avg_time[0]} to {avg_time[1]}s\n\n"
md_string += df_avgs.to_markdown()
with open(f"{path_folder}/{rk}.md", "w") as f:
    f.write(md_string)
# ------------------------------------------------------
