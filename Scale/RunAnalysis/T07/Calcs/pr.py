"""
pressure ratio
"""

# ------------------------------------------------------
# Calculations
def pressure_ratio(df):
    pt_exit_cols = ["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"]
    df["P_PT_Exit"] = df[pt_exit_cols].mean(axis=1)
    df["PR"] = (df["P_PT_Exit"] + 101.325) / 101.325

    df["speed_ratio"] = df["N_PLC_N2"] / df["ACC_NI_CH1_FFT"]

    df["P_Comb"] = (101.325 + df["P_NI_Combustor_Can_1"]) / (101.325 + df["P_PT_Exit"])

    return df