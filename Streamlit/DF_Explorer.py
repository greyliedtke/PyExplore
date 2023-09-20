"""
- read in csv file
- collect all columns
- select things to plot
- display in tabs

"""

# imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as go
import seaborn as sns

# Create matplotlib figures
def pf(
    df: pd.DataFrame,
    y_cols: list,
    x_col= "elapsed_sec",
    x_title="Elapsed Seconds",
    y_title="",
    title="",
    folder="test",
    x_lim=None,
    y_lim=None,
):
    # fig_spr = pf(df_results, "Compressor.RVD.RR", ["Compressor.RVD.SPR"], "RR", "SPR", x_lim=[1,2], title="SPR", folder=fstudy)
    fig, ax = plt.subplots()
    for i, y in enumerate(y_cols):
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
    plt.close()

    return fig


file = st.file_uploader("File Upload")

if file:

    # load dataframe and only when fuel
    df = pd.read_csv(file)
    cols = list(df.columns)

    st.divider()  

    p_select = st.multiselect("Columns", cols, default=cols[0])

    with st.expander("DF"):
        st.dataframe(df)
    with st.expander("Correlation"):
        # correlation map
        c_mat = st.multiselect("Columns", cols)
        if c_mat:
            dfc = df[c_mat]
            corr_matrix = dfc.corr()

            # Create the heatmap
            fig, ax = plt.subplots()
            fig.clear()
            cmpf = plt.matshow(corr_matrix, fig, cmap='coolwarm', interpolation='none')
            plt.colorbar()

            # Add xticks and yticks
            plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=90)
            plt.yticks(range(len(corr_matrix)), corr_matrix.columns)
            st.pyplot(fig)

    # create tabs from group column
    st.divider()

    # ------------------------------------------------------
    # STANDARD PLOTS

    x_col = st.selectbox("X axis", cols)
    pt = st.selectbox("Plot Type", ["Matplotlib", "Plotly"], 1)
    tabs = st.tabs(p_select)

    for i, p in enumerate(p_select):
        with tabs[i]:
            if pt == "Plotly":
                st.plotly_chart(go.scatter(df, x_col, p, title=p))
            elif pt == "Matplotlib":
                st.pyplot(pf(df, [p], x_col = x_col, title = p))
    # ------------------------------------------------------    
