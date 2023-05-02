"""
main file to operate control system
streamlit run ControlSystem/CC/Home.py
"""

import streamlit as st
import pandas as pd
import datetime

st.title("Home")


st.markdown("### Engine Test Queue")

st.markdown("### Test Path")

st.selectbox("Engine Mode", ["OFF", "Manual", "Auto"])


test_config = {
    "init_ao": 55,
    "PR_trigger":1.6,
    "init_n2": 15,
    "load_setting": 7
}

sensorTable = "populate with sensor stuff"

st.write(test_config)

start = st.time_input('Begin Test at', datetime.time(9, 30))
load_profile = {
    "load(kW)": [5, 10, 15, 20, 15, 10, 15, 20, 15, 10, 5],
    "duration(Min)": [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 25]
}
st.dataframe(load_profile)
