

def recuperator_summary(df):
    df["T_HP_Inlet"] = df["T_PT_Exit"]
    df["T_HP_Outlet"] = df[
        [
            "T_PLC_Recuperator_HP_Outlet_1",
            "T_PLC_Recuperator_HP_Outlet_2",
            "T_NI_Recuperator_HP_Outlet_3",
            "T_NI_Recuperator_HP_Outlet_4",
        ]
    ].mean(axis=1)
    df["T_LP_Inlet"] = df[["T_NI_LP_Inlet_1", "T_NI_LP_Inlet_2"]].mean(axis=1)
    df["T_LP_Outlet"] = df[["T_PLC_LP_Outlet_1", "T_NI_LP_Outlet_2"]].mean(axis=1)

    df["P_LP_Inlet"] = df[["P_NI_LP_Inlet_1", "P_NI_LP_Inlet_2"]].mean(axis=1)
    df["P_LP_Outlet"] = df[["P_NI_LP_Outlet_1", "P_NI_LP_Outlet_2"]].mean(axis=1)
    return df

