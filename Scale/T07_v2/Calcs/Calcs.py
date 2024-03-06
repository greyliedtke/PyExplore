"""
calculations for everything
"""

import pandas as pd

# ml /min to gph
h2232_lm = .016
h2232_kgs = h2232_lm * (.817/60)
h2232_gph = h2232_lm * (60/3.78541)

def target_pressure(row):
    # can increase pr if less than target n2
    if row["Target_N2"] >= row["N_PLC_N2"]:
        pr_target = 0.088 * row["CV_PLC_Passive_kW"] + 1.33
 
    # set target pr as ratio of target N2 and actual N2
    else:
        pr_target = 0.088 * row["CV_PLC_Passive_kW"] + 1.33 - .1*(row["Target_N2"]/row["N_PLC_N2"])

    return pr_target

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


def fuel_flow(df):
    rho_fuel = .817 # kg/m^3
    hhv = 43E3 # MJ/kg
    df['fuel_kgs'] = df['VF_PLC_Fuel'] * rho_fuel / 60
    df['fuel_gph'] = df['VF_PLC_Fuel'] * 60 / 3.78541 
    df['fuel_energy'] = df['fuel_kgs'] * hhv
    df["fuel_eff"] = 100 * (df["kw_4wi"] / df['fuel_energy'])
    return df


def calcs_darpa(df:pd.DataFrame):

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
    df["I_PLC"] = df[i_cols].sum(axis=1)/1000
    df["kw_4wi"] = df["I_PLC"] * 120
    df["kw_dt"] = -1*df["dt_pwr_mc"]
    df["kw_psu"] = df["PSU_P"]/1000
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

    df["PWR_DC"] = df["PLC_V_DC_Voltage"]*df["PLC_V_DC_Current"]/1000

    df["PWR_Expected"] = df["cc_ll_2"]*1.1

    df["PR_Target"] = 0.088 * (df["PWR_DC"]-1.5) + 1.33
    df["N2_Target"] = 0.7 * df["PWR_DC"] + 24

    df["PR_Error"] = df["cc_target_pr"] - df["cc_pr"]
    df["N2_Error"] = df["cc_target_n2"] - df["PLC_N_N2a"]

    df["N2_Delta"] = df["PLC_N_N2a"] - df["PLC_N_N2a"].shift(3)
    df["Time_Delta"] = df["elapsed_sec"] - df["elapsed_sec"].shift(3)
    df["N2_ACC"] = df["N2_Delta"] / df["Time_Delta"]

    df["N2_ACC_f"] = df["N2_ACC"].rolling(10).mean()

    return df

def calcs_t05(df:pd.DataFrame):

    # massflow calculation
    p_imp = ["P_Inlet_Mass_Flow_1_(Pa)", "P_Inlet_Mass_Flow_2_(Pa)"]
    df["P_Impeller"] = df[p_imp].mean(axis=1)
    p_imp.append("P_Impeller")
    df["P_Impeller"] = df["P_Impeller"] - df["P_Impeller"].iloc[0]
    # task05 had wrong calibration of 5 psi instead of 1 psi
    df["P_Impeller"] = df["P_Impeller"]*5

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
    v_cols = ["generator phase1 voltage", "generator phase2 voltage", "generator phase3 voltage"]
    df["voltage"] = df[v_cols].mean(axis=1)
    i_cols = ["generator phase1 current", "generator phase2 current", "generator phase3 current"]
    df["current"] = df[i_cols].sum(axis=1)
    df["power"] = df["current"]*df["voltage"]/1000

    return df


from scipy.signal import savgol_filter
# ------------------------------------------------------

# ------------------------------------------------------
# Calculations
def pressure_ratio(df):
    pt_exit_cols = ["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"]
    df["P_PT_Exit"] = df[pt_exit_cols].mean(axis=1)
    df["PR"] = (df["P_PT_Exit"] + 101.325) / 101.325

    df["speed_ratio"] = df['N_PLC_N2']/df['ACC_NI_CH1_FFT']

    df["P_Comb"] = (101.325+df["P_NI_Combustor_Can_1"])/(101.325+df["P_PT_Exit"])

    return df

def power(df):
    # Power calculations... zeroing out current readings
    i_cols = ["I_PLC_Phase_1", "I_PLC_Phase_2", "I_PLC_Phase_3"]
    for i in i_cols:
        df[i] = df[i] - df[i].iloc[0]
    # sum of all three phases
    df["I_PLC"] = df[i_cols].sum(axis=1)/1000
    df["kw_4wi"] = df["I_PLC"] * 120
    df["kw_dt"] = -1*df["dt_pwr_mc"]
    df["kw_psu"] = df["PSU_P"]/1000

    df["kw_lb"] = df["cc_ll"]*72/1000

    return df

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

def compressor_efficiency(df):
    df['T_Inlet'] = df[["T_PLC_Inlet_1", "T_NI_Inlet_2"]].mean(axis=1)
    df['T_PT_exit'] = df[["T_NI_PT_Exit_1", "T_NI_PT_Exit_2", "T_NI_PT_Exit_3", "T_NI_PT_Exit_4"]].mean(axis=1)
    t_rc = (df['T_PT_exit']+273.15)/(df['T_Inlet']+273.15)
    pr = df['PR']
    df['comp_eff_pt'] = ((pr**(.4/1.4)-1)/(t_rc-1))*100
    return df

def fuel_calcs(df):
    rho_fuel = .817 # kg/m^3
    hhv = 43E3 # MJ/kg
    df['fuel_kgs'] = df['VF_PLC_Fuel'] * rho_fuel / 60
    df['fuel_gph'] = df['VF_PLC_Fuel'] * 60 / 3.78541 
    df['fuel_energy'] = df['fuel_kgs'] * hhv
    df["fuel_eff"] = 100 * (df["kw_4wi"] / df['fuel_energy'])

    return df

def leakage(df):
    t_pt_ducts = ["T_PLC_PT_Outlet_Duct_1", "T_PLC_PT_Outlet_Duct_2", "T_NI_PT_Outlet_Duct_3", "T_NI_PT_Outlet_Duct_5", "T_NI_PT_Outlet_Duct_6", "T_NI_PT_Outlet_Duct_7"]
    df['T_PT_Duct'] = df[t_pt_ducts].mean(axis=1)

    df['T_PT_Exit'] = df[["T_NI_PT_Exit_1", "T_NI_PT_Exit_2", "T_NI_PT_Exit_3", "T_NI_PT_Exit_4"]].mean(axis=1)
    df['T_Bypass'] = df[["T_NI_Seal_Bypass_1", "T_NI_Seal_Bypass_3", "T_NI_Seal_Bypass_4"]].mean(axis=1)

    df['leakage'] = ((df['T_PT_Duct']-df['T_PT_Exit']) / (df['T_Bypass']-df['T_PT_Exit']))*100
    df['leakage_smooth'] = savgol_filter(df['leakage'], 20, 3) # window size 51, polynomial order 3
    return df

def cp_calc(p, t):
    # calculate cp from p and t
    # https://www.engineeringtoolbox.com/air-properties-d_156.html
    # return 1.006
    a = 1005.7
    b = .1074
    c = -.0455
    d = .00855

    cp = a + b*t + c*t**2 + d*t**3
    cp = cp/1000
    return cp

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

    df['T_LP_Inlet'] = df[["T_NI_LP_Inlet_1", "T_NI_LP_Inlet_2"]].mean(axis=1)
    Thi = df['T_LP_Inlet']

    df['T_HP_Outlet'] = df[["T_PLC_Recuperator_HP_Outlet_1", "T_PLC_Recuperator_HP_Outlet_2", "T_NI_Recuperator_HP_Outlet_3", "T_NI_Recuperator_HP_Outlet_4"]].mean(axis=1)
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

def recuperator_summary(df):
    df["T_HP_Inlet"] = df["T_PT_Exit"]
    df["T_HP_Outlet"] = df[["T_PLC_Recuperator_HP_Outlet_1", "T_PLC_Recuperator_HP_Outlet_2", "T_NI_Recuperator_HP_Outlet_3", "T_NI_Recuperator_HP_Outlet_4"]].mean(axis=1)
    df["T_LP_Inlet"] = df[["T_NI_LP_Inlet_1", "T_NI_LP_Inlet_2"]].mean(axis=1)
    df["T_LP_Outlet"] = df[["T_PLC_LP_Outlet_1", "T_NI_LP_Outlet_2"]].mean(axis=1)

    df["P_LP_Inlet"] = df[["P_NI_LP_Inlet_1", "P_NI_LP_Inlet_2"]].mean(axis=1)
    df["P_LP_Outlet"] = df[["P_NI_LP_Outlet_1", "P_NI_LP_Outlet_2"]].mean(axis=1)
    return df

# ------------------------------------------------------

# ------------------------------------------------------
# process to attempt all calcs
def calcs_t07(df:pd.DataFrame):
    calculations = [power, massflow, pressure_ratio, compressor_efficiency, leakage, fuel_calcs, recuperator_efficiency, recuperator_summary]

    for calc in calculations:
        try:
            df = calc(df)
        except Exception as e:
            print(f"----------ENCOUNTERED---------: {e}")
            pass

    return df
# -----------------------------------------------------