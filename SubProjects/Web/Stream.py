"""
- control lights
"""

# imports
import streamlit as st
import time
import keyboard



st_check = st.checkbox("Time Calller")


def send_color(k):
    lc = st.session_state.get(k)
    print(lc)

light_color = st.color_picker("Light Color")
p_index = st.number_input("Pixel number", value=1)


if st_check:
    print(light_color, p_index)
    st.experimental_rerun()
