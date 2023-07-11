"""
streamlit run PiRoom/Home.py
"""

import streamlit as st

simulate = True
if not simulate:
    import pipixels


st.markdown("### Light controls")

s1_color = st.color_picker("Strip 1 Color", value="#F9D7A4")
s1_b = st.button("Send")

if s1_b:
    print(s1_color)