def leakage(df):
    t_pt_ducts = [
        "T_PLC_PT_Outlet_Duct_1",
        "T_PLC_PT_Outlet_Duct_2",
        "T_NI_PT_Outlet_Duct_3",
        "T_NI_PT_Outlet_Duct_5",
        "T_NI_PT_Outlet_Duct_6",
        "T_NI_PT_Outlet_Duct_7",
    ]
    df["T_PT_Duct"] = df[t_pt_ducts].mean(axis=1)

    df["T_PT_Exit"] = df[
        ["T_NI_PT_Exit_1", "T_NI_PT_Exit_2", "T_NI_PT_Exit_3", "T_NI_PT_Exit_4"]
    ].mean(axis=1)
    df["T_Bypass"] = df[
        ["T_NI_Seal_Bypass_1", "T_NI_Seal_Bypass_3", "T_NI_Seal_Bypass_4"]
    ].mean(axis=1)

    df["leakage"] = (
        (df["T_PT_Duct"] - df["T_PT_Exit"]) / (df["T_Bypass"] - df["T_PT_Exit"])
    ) * 100
    df["leakage_smooth"] = savgol_filter(
        df["leakage"], 20, 3
    )  # window size 51, polynomial order 3
    return df