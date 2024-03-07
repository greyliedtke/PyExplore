"""
script for plotting many things...
"""
import matplotlib.pyplot as plt
from sklearn import linear_model

# ------------------------------------------------------
# Create trend
def create_trend(df, x_col, y_col, title, x_label, y_label, save=None):
    X = df[[x_col]]
    Y = df[[y_col]]
    lr = linear_model.LinearRegression()
    lr.fit(X, Y)
    trend_text = f"{y_label} = {round(lr.coef_[0][0], 2)} * {x_label} + {round(lr.intercept_[0], 2)}"
    print(trend_text)
    df[f"{y_col}_trend"] = lr.predict(X)

    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.plot(df[x_col], df[f"{y_col}_trend"])
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.text(0.1, 0.8, trend_text, horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
    ax.grid()
    if save:
        fig.savefig(f"{save}/figs/{title}.png")
    return fig
# ------------------------------------------------------


# Genertic creating figure for multiple columns
def pf(df, x_col, y_cols, x_title="", y_title="", title="", x_lim=None, y_lim=None, save=None):
    # fig_spr = pf(df_results, "Compressor.RVD.RR", ["Compressor.RVD.SPR"], "RR", "SPR", x_lim=[1,2], title="SPR", folder=fstudy)
    fig, ax = plt.subplots()
    for y in y_cols:
        ax.plot(df[x_col], df[y])

    if y_lim != [0, 0]:
        ax.set_ylim(y_lim)
    if x_lim != [0, 0]:
        ax.set_xlim(x_lim)

    ax.legend(y_cols)
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.grid()
    if save:
        fig.savefig(f"{save}/figs/{title}.png")
    return fig
# ------------------------------------------------------


plot_dict = {
    "PR": {"Units": "psi", "Cols": ["PR", "cc_target_pr"]},
    "N1": {"Units": "kRPM", "Cols": ["N_PLC_N1", "ACC_NI_CH1_FFT"]},
    "N2": {"Units": "kRPM", "Cols": ["N_PLC_N2", "cc_target_n2"]},
    "Speed_Ratio": {"Units": "%", "Limits": [0, 1], "Cols": ["speed_ratio"]},
    "Massflow": {"Units": "kg/s", "Cols": ["MF_Impeller", "MF_Bellmouth"]},
    "Compressor Efficiency": {"Units": "%", "Cols": ["comp_eff_pt"]},
    "Leakage": {"Units": "kg/s", "Cols": ["leakage_smooth"]},
    "Voltage": {
        "Units": "V",
        "Cols": ["V_PLC_Phase_1", "V_PLC_Phase_2", "V_PLC_Phase_3"],
    },
    "Current": {
        "Units": "A",
        "Cols": ["I_PLC_Phase_1", "I_PLC_Phase_2", "I_PLC_Phase_3"],
    },
    "Power": {"Units": "kW", "Cols": ["PSU_P"]},
    "Power_Load": {"Units": "kW", "Cols": ["kw_4wi"]},
    "Recuperator_Eff": {"Units": "kW", "Cols": ["recuperator_eff"]},
    "Current_PSU": {"Units": "kW", "Cols": ["PSU_I"]},
    "Load_Level": {"Units": "int", "Cols": ["cc_ll"]},
    "P_Comb": {"Units": "int", "Cols": ["P_Comb"]},
    "DT_Load": {"Units": "%", "Cols": ["dt_load_mc"]},
    "DC_Voltage": {"Units": "V DC", "Cols": ["PSU_V", "dt_u_mc"]},
    "DT_Power": {"Units": "kw", "Cols": ["dt_pwr_mc"]},
    "P_Bellmouth": {"Units": "kPa", "Cols": ["P_PLC_Bellmouth_1", "P_NI_Bellmouth_2"]},
    "P_Inlet": {
        "Units": "kPa",
        "Cols": ["P_PLC_Inlet_MF", "P_NI_Inlet_Mass_Flow_2", "P_NI_Inlet_Mass_Flow_3"],
    },
    "P_Impeller_Inlet": {
        "Units": "kPa",
        "Cols": [
            "P_NI_Impeller_Exit_1",
            "P_NI_Impeller_Exit_2",
            "P_NI_Impeller_Exit_3",
            "P_NI_Impeller_Exit_4",
        ],
    },
    "P_Lab_Seal_Upstream": {
        "Units": "kPa",
        "Cols": [
            "P_NI_Lab_Seal_Upstream_1",
            "P_NI_Lab_Seal_Upstream_2",
            "P_NI_Lab_Seal_Upstream_3",
            "P_NI_Lab_Seal_Upstream_4",
        ],
    },
    "P_Lab_Seal_Downstream": {
        "Units": "kPa",
        "Cols": [
            "P_NI_Lab_Seal_Downstream_1",
            "P_NI_Lab_Seal_Downstream_2",
            "P_NI_Lab_Seal_Downstream_3",
            "P_NI_Lab_Seal_Downstream_4",
        ],
    },
    "P_PT_Exit": {
        "Units": "kPa",
        "Cols": ["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"],
    },
    "P_Combustor": {"Units": "kPa", "Cols": ["P_NI_Combustor_Can_1"]},
    "P_Turbine_Diffuser_Exit": {
        "Units": "kPa",
        "Cols": ["P_PLC_Turbine_Diffuser_Exit_1", "P_NI_Turbine_Diffuser_Exit_2"],
    },
    "P_LP_Inlet": {"Units": "kPa", "Cols": ["P_NI_LP_Inlet_1", "P_NI_LP_Inlet_2"]},
    "P_LP_Outlet": {"Units": "kPa", "Cols": ["P_NI_LP_Outlet_1", "P_NI_LP_Outlet_2"]},
    "P_Hot_Section_Housing_1": {
        "Units": "kPa",
        "Cols": ["P_NI_Hot_Section_Housing_1", "P_NI_Hot_Section_Housing_2"],
    },
}
