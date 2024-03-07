



def recuperator_efficiency(df):
    """
    eff = (Tco-Tci)/(Thi-Tci)
    Thi = EGT or recuperator LP inlet temp
    Tco = combustor inlet temperature / recuperator HP outlet temp
    Tci = recuperator HP inlet temp / PT outlet temp

    eff=(Ch*(Thi-Tho))/(Cmin*(Thi-Tci))

    Ch= Cp (at Th-ave = (Thi+Tho)/2) * LP side massflow (should be roughly 1.01x HP side massflow)
    Cmin= Cp (at Tc-ave = (Tci+Tco)/2) * HP side massflow
    Tho= recuperator LP exhaust (if you measure this)

    """

    df["T_LP_Inlet"] = df[["T_NI_LP_Inlet_1", "T_NI_LP_Inlet_2"]].mean(axis=1)
    Thi = df["T_LP_Inlet"]

    df["T_HP_Outlet"] = df[
        [
            "T_PLC_Recuperator_HP_Outlet_1",
            "T_PLC_Recuperator_HP_Outlet_2",
            "T_NI_Recuperator_HP_Outlet_3",
            "T_NI_Recuperator_HP_Outlet_4",
        ]
    ].mean(axis=1)
    Tco = df["T_HP_Outlet"]

    Tci = df["T_PT_Duct"]

    df["recuperator_eff"] = 100 * (Tco - Tci) / (Thi - Tci)

    # including massflow energy balance
    # Th = (Thi+Tco)/2
    # Tc = (Tci+Tco)/2

    # # assuming constnt Cp for now...
    # lp_mf = df['MF_Bellmouth']
    # hp_mf = lp_mf/1.01
    # Ch = cp_calc(1, Th) * lp_mf
    # Cmin = cp_calc(1, Tc) * hp_mf
    # Tho = df['T_NI_LP_Outlet_2']

    # df['recuperator_eff_mf'] = 100*(Ch*(Thi-Tho))/(Cmin*(Thi-Tci))

    return df