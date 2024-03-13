"""
creating general data plotter

"""

# ------------------------------------------------------
# Imports
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
# ------------------------------------------------------

# ------------------------------------------------------
# dataframes
df = pd.read_csv("Web/data.csv")

# plotting
x_col = st.selectbox("x_col", list(df.columns))
y_cols = st.multiselect("y_cols", list(df.columns), list(df.columns)[0])

with st.expander("Labels"):
    title = st.text_input("Plot Title")
    x_label = st.text_input("x label", x_col)
    y_label = st.text_input("y label", y_cols[0])
    
with st.expander("Format"):
    scatter = st.checkbox("Scatter")
    x_lim = st.text_input("x_lim", "[0,0]")
    y_lim = st.text_input("y_lim", "[0,0]")
    legend = st.text_input("legend", y_cols)
    grid = st.checkbox("grid", value=True)

fig, ax = plt.subplots()
pt = ""
pt += "fig, ax = plt.subplots()\n"

if len(y_cols)>1:
    for i, y in enumerate(y_cols):
        if scatter:
            ax.scatter(df[x_col], df[y])
            pt += f"ax.scatter(df['{x_col}'], df['{y}'])\n"
        else:
            ax.plot(df[x_col], df[y])
            pt += f"ax.plot(df['{x_col}'], df['{y}'])\n"
else:
    if scatter:
        ax.scatter(df[x_col], df[y_cols[0]])
        pt += f"ax.scatter(df['{x_col}'], df['{y_cols[0]}'])\n"
    else:
        ax.plot(df[x_col], df[y_cols[0]])
        pt += f"ax.plot(df['{x_col}'], df['{y_cols[0]}'])\n"

ax.set_xlabel(x_label)
pt += f"ax.set_xlabel('{x_label}')\n"
ax.set_ylabel(y_label)
pt += f"ax.set_ylabel('{y_label}')\n"
if title: 
    ax.set_title(title)
    pt += f"ax.set_title('{title}')\n"
if legend: 
    ax.legend(eval(legend))
    pt += f"ax.legend({legend}))\n"
if grid: 
    ax.grid()
    pt += f"ax.grid()\n"
if x_lim != "[0,0]":
    ax.set_xlim(eval(x_lim))
    pt += f"ax.set_xlim({x_lim})\n"
if y_lim != "[0,0]":
    ax.set_ylim(eval(y_lim))
    pt += f"ax.set_ylim({y_lim})\n"


st.pyplot(fig)
st.code(f"""
import matplotlib.pyplot as plt
        
df = pd.read_csv("data.csv")

{pt}     

""")
