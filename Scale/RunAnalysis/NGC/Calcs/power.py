"""

"""

def power(df):
    # Power calculations... zeroing out current readings
    i_cols = ["I_PLC_Phase_1", "I_PLC_Phase_2", "I_PLC_Phase_3"]
    for i in i_cols:
        df[i] = df[i] - df[i].iloc[0]
    # sum of all three phases
    df["I_PLC"] = df[i_cols].sum(axis=1) / 1000
    df["kw_4wi"] = df["I_PLC"] * 120
    # df["kw_dt"] = -1 * df["dt_pwr_mc"]
    # df["kw_psu"] = df["PSU_P"] / 1000
    df["kw_lb"] = df["cc_ll"] * 72 / 1000
    return df

