

def compressor_efficiency(df):
    df["T_Inlet"] = df[["T_PLC_Inlet_1", "T_NI_Inlet_2"]].mean(axis=1)
    df["T_PT_exit"] = df[
        ["T_NI_PT_Exit_1", "T_NI_PT_Exit_2", "T_NI_PT_Exit_3", "T_NI_PT_Exit_4"]
    ].mean(axis=1)
    t_rc = (df["T_PT_exit"] + 273.15) / (df["T_Inlet"] + 273.15)
    pr = df["PR"]
    df["comp_eff_pt"] = ((pr ** (0.4 / 1.4) - 1) / (t_rc - 1)) * 100
    return df