"""
calculations for everything
"""

import pandas as pd

# ml /min to gph
h2232_lm = 0.016
h2232_kgs = h2232_lm * (0.817 / 60)
h2232_gph = h2232_lm * (60 / 3.78541)


def target_pressure(row):
    # can increase pr if less than target n2
    if row["Target_N2"] >= row["N_PLC_N2"]:
        pr_target = 0.088 * row["CV_PLC_Passive_kW"] + 1.33

    # set target pr as ratio of target N2 and actual N2
    else:
        pr_target = (
            0.088 * row["CV_PLC_Passive_kW"]
            + 1.33
            - 0.1 * (row["Target_N2"] / row["N_PLC_N2"])
        )

    return pr_target

def calcs_darpa(df: pd.DataFrame):

    # initialize parameters. is impeller area the same?
    imp_area = 0.00314411  # m^2
    imp_area_factor = 0.9  # impeller af

    bm_area = 3.14159 * (5 * 0.0254) ** 2 / 4  # m^2
    bm_area_factor = 0.90  # bm af

    pt_exit_cols = ["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"]
    df["PR"] = (df[pt_exit_cols].mean(axis=1) + 101.325) / 101.325

    i_cols = ["I_PLC_Phase_1", "I_PLC_Phase_2", "I_PLC_Phase_3"]
    for i in i_cols:
        df[i] = df[i] - df[i].iloc[0]
    # sum of all three phases
    df["I_PLC"] = df[i_cols].sum(axis=1) / 1000
    df["kw_4wi"] = df["I_PLC"] * 120
    df["kw_dt"] = -1 * df["dt_pwr_mc"]
    df["kw_psu"] = df["PSU_P"] / 1000
    # df["Target_PR"] = 0.088 * df["CV_PLC_Passive_kW"] + 1.33
    # df["Target_N2"] = 0.62 * df["CV_PLC_Passive_kW"] + 21.7
    # df["Target_PR_f"] = [target_pressure(row) for i, row in df.iterrows()]

    try:
        df["P_Impeller"] = df[
            ["P_NI_Inlet_Mass_Flow_2", "P_NI_Inlet_Mass_Flow_3"]
        ].mean(axis=1)
        df["P_BM"] = df[["P_PLC_Bellmouth_1", "P_NI_Bellmouth_2"]].mean(axis=1)

        # massflow calculation
        df["MF_Impeller"] = [
            mass_flow_calc(
                101.325,
                20,
                -row["P_Impeller"],
                inlet_temp=20,
                area=imp_area,
                cd=imp_area_factor,
            )
            for i, row in df.iterrows()
        ]
        df["MF_Bellmouth"] = [
            mass_flow_calc(
                101.325,
                20,
                -row["P_BM"],
                inlet_temp=20,
                area=bm_area,
                cd=bm_area_factor,
            )
            for i, row in df.iterrows()
        ]
    except:
        print("cannout compute")

    return df


def calcs_ngc(df: pd.DataFrame):
    pt_exit_cols = [
        "PLC_PT_Exit_Flow_1",
        "PLC_PT_Exit_Flow_2",
        "PLC_PT_Exit_Flow_3",
        "PLC_PT_Exit_Flow_4",
    ]
    df["PR"] = (df[pt_exit_cols].mean(axis=1)) / 101.325

    i_cols = [
        "PLC_V_Phase_1_Current",
        "PLC_V_Phase_2_Current",
        "PLC_V_Phase_3_Current",
        "PLC_V_Phase_1b_Current",
        "PLC_V_Phase_2b_Current",
        "PLC_V_Phase_3b_Current",
    ]

    df["PWR_DC"] = df["PLC_V_DC_Voltage"] * df["PLC_V_DC_Current"] / 1000

    df["PWR_Expected"] = df["cc_ll_2"] * 1.1

    df["PR_Target"] = 0.088 * (df["PWR_DC"] - 1.5) + 1.33
    df["N2_Target"] = 0.7 * df["PWR_DC"] + 24

    df["PR_Error"] = df["cc_target_pr"] - df["cc_pr"]
    df["N2_Error"] = df["cc_target_n2"] - df["PLC_N_N2a"]

    df["N2_Delta"] = df["PLC_N_N2a"] - df["PLC_N_N2a"].shift(3)
    df["Time_Delta"] = df["elapsed_sec"] - df["elapsed_sec"].shift(3)
    df["N2_ACC"] = df["N2_Delta"] / df["Time_Delta"]

    df["N2_ACC_f"] = df["N2_ACC"].rolling(10).mean()

    return df


def calcs_t05(df: pd.DataFrame):

    # massflow calculation
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


from scipy.signal import savgol_filter



# ------------------------------------------------------
# process to attempt all calcs
def calcs_t07(df: pd.DataFrame):
    calculations = [
        power,
        massflow,
        pressure_ratio,
        compressor_efficiency,
        leakage,
        fuel_calcs,
        recuperator_efficiency,
        recuperator_summary,
    ]

    for calc in calculations:
        try:
            df = calc(df)
        except Exception as e:
            print(f"----------ENCOUNTERED---------: {e}")
            pass

    return df


# -----------------------------------------------------
