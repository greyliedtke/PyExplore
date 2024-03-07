import pandas as pd

def mass_flow_calc(amb_p, amb_t, inlet_pressure, inlet_temp, area, cd):
    # df['imp_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=imp_area, cd=imp_area_factor) for inlet_p in imp_pressure_avg_pa]
    # df['bm_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=bm_area, cd=bm_area_factor) for inlet_p in bm_avg_pa]
    # all variables in si units. https://www.grc.nasa.gov/www/k-12/rocket/mflchk.html. rearrange and include cd...
    p_ratio = (inlet_pressure + amb_p)/amb_p
    m_local = (2 * (p_ratio ** (-.4/1.4) - 1)/.4) ** .5
    mass_flow = (cd * area * amb_p / (amb_t ** .5)) * ((1.4 / inlet_temp) ** .5) * m_local * \
                ((1 + (.2 * (m_local ** 2))) ** (-.5 * 2.4 / .4))
    mass_flow = mass_flow.real
    return mass_flow

def calcs_t05(df: pd.DataFrame):

    # massflow calculation
    try:
        p_imp = ["P_Inlet_Mass_Flow_1_(Pa)", "P_Inlet_Mass_Flow_2_(Pa)"]
        df["P_Impeller"] = df[p_imp].mean(axis=1)
        p_imp.append("P_Impeller")
        df["P_Impeller"] = df["P_Impeller"] - df["P_Impeller"].iloc[0]
        # task05 had wrong calibration of 5 psi instead of 1 psi
        df["P_Impeller"] = df["P_Impeller"] * 5

        imp_area = 0.00314411  # m^2
        imp_area_factor = 0.9  # impeller af
        df["MF_Impeller"] = [
            mass_flow_calc(
                101.325,
                20,
                row["P_Impeller"],
                inlet_temp=20,
                area=imp_area,
                cd=imp_area_factor,
            )
            for i, row in df.iterrows()
        ]
    except:
        print("Check mf impeller calculation")

    # power calculation
    v_cols = [
        "generator phase1 voltage",
        "generator phase2 voltage",
        "generator phase3 voltage",
    ]
    df["voltage"] = df[v_cols].mean(axis=1)
    i_cols = [
        "generator phase1 current",
        "generator phase2 current",
        "generator phase3 current",
    ]
    df["current"] = df[i_cols].sum(axis=1)
    df["power"] = df["current"] * df["voltage"] / 1000

    return df