"""
file for creating fuel spillback system testing
"""

import asyncio
import streamlit as st
import time
from datetime import datetime

st.title("Fuel system testing")

valve_slider = st.slider("Proportional Valve", min_value=0, max_value=100, key="p_valve")

fuel_slider = st.slider("Fuel Signal", min_value=0, max_value=100)


send_button = st.button("Send commands", on_click=lambda: send_cmds())
slider = st.button("Send slide", on_click=lambda: rate_change())

def rate_change():
    time.sleep(.5)
    st.slider('slider', 0, 10, value = st.session_state.p_valve, key='slidey')

def send_cmds():
    print(valve_slider, fuel_slider)

async def clock():
    while True:
        tn = datetime.now()
        print(tn)
        await asyncio.sleep(1)
    
asyncio.run(clock())
