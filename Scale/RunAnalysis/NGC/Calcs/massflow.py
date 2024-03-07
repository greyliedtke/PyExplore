
# ------------------- Massflow -----------------------------------------
def mass_flow_calc(amb_p, amb_t, inlet_pressure, inlet_temp, area, cd):
    # df['imp_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=imp_area, cd=imp_area_factor) for inlet_p in imp_pressure_avg_pa]
    # df['bm_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=bm_area, cd=bm_area_factor) for inlet_p in bm_avg_pa]
    # all variables in si units. https://www.grc.nasa.gov/www/k-12/rocket/mflchk.html. rearrange and include cd...
    p_ratio = (inlet_pressure + amb_p)/amb_p
    m_local = (2 * (p_ratio ** (-.4/1.4) - 1)/.4) ** .5
    mass_flow = (cd * area * amb_p / (amb_t ** .5)) * ((1.4 / inlet_temp) ** .5) * m_local * \
                ((1 + (.2 * (m_local ** 2))) ** (-.5 * 2.4 / .4))
    return mass_flow

def massflow(df):
    # initialize parameters. is impeller area the same?
    imp_area = 0.00314411  # m^2
    imp_area_factor = 0.9  # impeller af

    bm_area = 3.14159 * (5 * 0.0254) ** 2 / 4  # m^2
    bm_area_factor = 0.90  # bm af

    ambient_temp = 20 + 273.15 # deg C

    df["P_Impeller"] = df[
            ["P_NI_Inlet_Mass_Flow_2", "P_NI_Inlet_Mass_Flow_3"]
        ].mean(axis=1)
    df["P_BM"] = df[["P_PLC_Bellmouth_1", "P_NI_Bellmouth_2"]].mean(axis=1)

    # massflow calculation
    df["MF_Impeller"] = [
        mass_flow_calc(
            101325,
            ambient_temp,
            -1000*row["P_Impeller"],
            inlet_temp=row["T_NI_Inlet_2"]+273.15,
            area=imp_area,
            cd=imp_area_factor,
        )
        for i, row in df.iterrows()
    ]
    df["MF_Bellmouth"] = [
        mass_flow_calc(
            101325,
            ambient_temp,
            -1000*row["P_BM"],
            inlet_temp=row["T_NI_Inlet_2"]+273.15,
            area=bm_area,
            cd=bm_area_factor,
        )
        for i, row in df.iterrows()
    ]
    return df