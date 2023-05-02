import streamlit as st
import pandas as pd
from DataProcessing.FigureGenerator import fig_plotter, sensor_fusion
from csv_logger import CsvLogger

plot_df = pd.read_excel("ControlSystem/CC/DataProcessing/Figure_Template.xlsx")

csv_log = CsvLogger(
    "ControlSystem/TestLog/test_log.csv",
    header=["date", "log", "value"],
    fmt=f"%(asctime)s,%(levelname)s,%(message)s")

def save_report(df:pd.DataFrame, test_name:str, test_desc:str, test_time:str):
    # function to save report in folder and add to log
    # initialize logging file
    df.to_csv(f"{'ControlSystem/TestLog/TestData'}/{test_name}.csv")
    csv_log.runs([test_name, test_desc, test_time])

def spi_report(df:pd.DataFrame):
    """
    df: run dataframe
    try to generate massive report from dataframe...
    """
    # report calculations
    df_cols = list(df.columns)
    if "P_PLC_PT_Exit_1" in df_cols:
        avg_pt = df[["P_PLC_PT_Exit_1", "P_PLC_PT_Exit_2", "P_PLC_PT_Exit_3"]].mean(axis=1)
        df["PR"] = (avg_pt + 101.325) / 101.325
    if "VF_PLC_Fuel" in df_cols:
        df["fuel_gph"] = df["VF_PLC_Fuel"] * 60 / 3.78541
        df["fuel_kgs"] = df["VF_PLC_Fuel"] * 0.817 / 60

    plot_groups = plot_df['Group'].unique()
    for group in plot_groups:

        # Adding to Table of contents, creating header, and adding table columns for 3 cols
        fig_col_i = 0  # table column
        st.markdown(f"### {group}")
        fig_cols = st.columns(3)

        for i, row in plot_df[plot_df['Group']==group].iterrows():

            # try to create figure
            try:

                y_cols = eval(row["y"])

                if len(y_cols)>1:
                    df = sensor_fusion(df, eval(row["y"]), row["title"])
                    y_cols.append(row["title"])


                title = row["title"]
                fig = fig_plotter(
                        df,
                        row["x"],
                        eval(row["y"]),
                        row["x_label"],
                        row["y_label"],
                        title,
                        row["Expected_range"],
                    )
                with fig_cols[fig_col_i]:
                    st.pyplot(fig, clear_figure=True)

                fig_col_i+= 1
                if fig_col_i == 3: 
                    fig_col_i=0
    
            except Exception as e:
                print(f'failed to create: {row["title"]} because {e}')

    return df
        