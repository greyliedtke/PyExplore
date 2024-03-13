# ------------------- Massflow -----------------------------------------
def mass_flow_calc(amb_p, amb_t, inlet_pressure, inlet_temp, area, cd):
    # df['imp_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=imp_area, cd=imp_area_factor) for inlet_p in imp_pressure_avg_pa]
    # df['bm_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=bm_area, cd=bm_area_factor) for inlet_p in bm_avg_pa]
    # all variables in si units. https://www.grc.nasa.gov/www/k-12/rocket/mflchk.html. rearrange and include cd...
    p_ratio = (inlet_pressure + amb_p) / amb_p
    m_local = (2 * (p_ratio ** (-0.4 / 1.4) - 1) / 0.4) ** 0.5
    mass_flow = (
        (cd * area * amb_p / (amb_t**0.5))
        * ((1.4 / inlet_temp) ** 0.5)
        * m_local
        * ((1 + (0.2 * (m_local**2))) ** (-0.5 * 2.4 / 0.4))
    )
    return mass_flow


def massflow(df):
    # initialize parameters. is impeller area the same?
    imp_area = 0.00314411  # m^2
    imp_area_factor = 0.9  # impeller af

    bm_area = 3.14159 * (5 * 0.0254) ** 2 / 4  # m^2
    bm_area_factor = 0.90  # bm af

    ambient_temp = 20 + 273.15  # deg C

    if "P_PLC_Bellmouth_1" in df.columns:
        df["P_Impeller"] = df[
            ["P_NI_Inlet_Mass_Flow_2", "P_NI_Inlet_Mass_Flow_3"]
        ].mean(axis=1)
        df["P_BM"] = df[["P_PLC_Bellmouth_1", "P_NI_Bellmouth_2"]].mean(axis=1)
    elif "P_PLC_Bellmouth_Pressure_1" in df.columns:
        df["P_Impeller"] = df[
            ["P_NI_Inlet_Mass_Flow_2", "P_NI_Inlet_Mass_Flow_3"]
        ].mean(axis=1)
        df["P_BM"] = df[
            ["P_PLC_Bellmouth_Pressure_1", "P_NI_Bellmouth_Pressure_2"]
        ].mean(axis=1)

    # massflow calculation
    df["MF_Impeller"] = [
        mass_flow_calc(
            101325,
            ambient_temp,
            -1000 * row["P_Impeller"],
            inlet_temp=row["T_NI_Inlet_2"] + 273.15,
            area=imp_area,
            cd=imp_area_factor,
        )
        for i, row in df.iterrows()
    ]
    df["MF_Bellmouth"] = [
        mass_flow_calc(
            101325,
            ambient_temp,
            -1000 * row["P_BM"],
            inlet_temp=row["T_NI_Inlet_2"] + 273.15,
            area=bm_area,
            cd=bm_area_factor,
        )
        for i, row in df.iterrows()
    ]
    return df


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
    # summarize temperatures and pressures
    df["T_HP_Inlet"] = df["T_PT_Exit"]
    df["T_HP_Outlet"] = df[["T_PLC_Recuperator_HP_Outlet_1", "T_PLC_Recuperator_HP_Outlet_2", "T_NI_Recuperator_HP_Outlet_3", "T_NI_Recuperator_HP_Outlet_4"]].mean(axis=1)
    df["T_LP_Inlet"] = df[["T_NI_LP_Inlet_1", "T_NI_LP_Inlet_2"]].mean(axis=1)
    df["T_LP_Outlet"] = df[["T_PLC_LP_Outlet_1", "T_NI_LP_Outlet_2"]].mean(axis=1)
    df["P_LP_Inlet"] = df[["P_NI_LP_Inlet_1", "P_NI_LP_Inlet_2"]].mean(axis=1)
    df["P_LP_Outlet"] = df[["P_NI_LP_Outlet_1", "P_NI_LP_Outlet_2"]].mean(axis=1)

    # calculate recuperator efficiency
    Thi = df['T_LP_Inlet']
    Tco = df['T_HP_Outlet']
    Tci = df['T_PT_Duct']
    df['recuperator_eff'] = 100*(Tco-Tci)/(Thi-Tci)

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
