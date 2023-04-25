"""
streamlit run Fuzzy/Pi/stream.py
"""


import streamlit as st
import pandas as pd
import numpy as np
import time


def send_servo():
    print(s_slider)


st.title('Servo Control')
s_slider = st.slider('Servo', 0, 180, value=90, step=1, on_change=lambda: send_servo())


