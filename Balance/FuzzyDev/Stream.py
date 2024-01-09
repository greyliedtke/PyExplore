"""
creating streamlit for fuzzy design
"""
import streamlit as st
import matplotlib.pyplot as plt
# from PSU import fc_psu, m_psu, r_psu, m_pr_d
from Th import fc_theta
import numpy as np
st.set_option('deprecation.showPyplotGlobalUse', False)

a_out = []

th_range = np.linspace(-30,30)

for i in th_range:
    out = fc_theta.compute(i)
    a_out.append(out)

fig, ax = plt.subplots()
ax.plot(th_range, a_out)
ax.set_xlabel('TH Error')
ax.set_ylabel('Servo Response')
ax.set_title("System Response")
ax.grid()
st.pyplot(fig)

# a_out = []

# for i in r_psu:
#     out = fc_psu.compute(i)
#     a_out.append(out)

# fig, ax = plt.subplots()
# ax.plot(r_psu, a_out)
# ax.set_xlabel('PSU Power')
# ax.set_ylabel('PR delta')
# ax.set_title("PSU PR Response")
# ax.grid()
# st.pyplot(fig)

# # membership functions
# with st.expander('Membership functions'):
#     st.pyplot(m_psu.view())
#     st.pyplot(m_pr_d.view())
