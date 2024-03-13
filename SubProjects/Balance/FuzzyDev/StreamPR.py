"""
creating streamlit for fuzzy design
"""
import streamlit as st
import matplotlib.pyplot as plt
from DCRB import fc_vb
import numpy as np

st.set_option("deprecation.showPyplotGlobalUse", False)



power = st.slider("Power", 0, 15)
# establish baseline pr value
pr_target = round(power * 0.088 + 1.33, 2)
st.metric("PR Target", pr_target)

# pr_delta = pr_target - pr_reading
n2_err = st.slider("N2 err", -4.0, 4.0, 0.0)
n2_acc = st.slider("N2 acc", -0.5, 0.5, 0.0)
pr_delta = st.slider("PR Delta", -0.2, 0.2, 0.0)

th_range = np.linspace(-.2, .2)

a_out = []
for i in th_range:
    out = fc_vb.compute({"n2_err": n2_err, "n2_acc": n2_acc, "PR_delta": i})
    a_out.append(out)

fig, ax = plt.subplots()
ax.plot(th_range, a_out)
ax.set_xlabel("PR Error")
ax.set_ylabel("PR Delta Response")
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
