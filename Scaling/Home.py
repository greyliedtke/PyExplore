"""
main file to operate control system
streamlit run ControlSystem/CC/Home.py
"""

import streamlit as st
import streamlit as st
import datetime

st.title("Home")


st.markdown("### Engine Test Queue")

st.markdown("### Test Path")

st.selectbox("Engine Mode", ["OFF", "Manual", "Auto"])

start = st.time_input('Begin Test at', datetime.time(9, 30))
load_profile = {
    "load(kW)": [5, 10, 15, 20, 15, 10, 15, 20, 15, 10, 5],
    "duration(Min)": [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 25]
}
st.dataframe(load_profile)

# test sequencer
st.markdown("""
- Initialize test
- lightoff
- Idle
- If PR > 1.5
- If N2 > 5

- Enter power --> calculate target N2
- pay attention to Turbine exit, temperatures, stability


""")