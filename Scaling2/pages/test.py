



import streamlit as st
import datetime

st.title('Test Screen')

def power_to_n2(power: float):
    # function to convert power setpoint to n2 reading
    # power(kw) = 13.41x - 20.74
    pr = (power+20.74)/13.4
    pr = round(pr, 1)
    st.metric("Targe PR (%)", pr)


st.button('Stop')
st.button('Start')
power_input = st.slider('Power Input (kW)', min_value=0, max_value=30)

turbine_exit = st.slider('Turbine Exit Sim (C)', min_value=600, max_value=900)


if power_input:
    power_to_n2(power_input)



