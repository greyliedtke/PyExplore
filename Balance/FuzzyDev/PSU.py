"""
creating fuzzy controller for PR and fuel control
"""
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
from Control.FuzzyDev.FuzzyClass import FuzzyController

# pr output
pr_lim = 1
p_pr_d = np.linspace(-pr_lim, pr_lim, 100)
m_pr_d = ctrl.Consequent(p_pr_d, 'PR_delta')
m_pr_d['increase'] = fuzz.trimf(p_pr_d, [0, pr_lim, pr_lim])
m_pr_d['decrease'] = fuzz.trimf(p_pr_d, [-pr_lim, -pr_lim, 0])
m_pr_d['nochange'] = fuzz.trimf(p_pr_d, [-pr_lim, 0, pr_lim])


# ------------------------------------------------------
# PR
psu_lim = 2
r_psu = np.linspace(-psu_lim, psu_lim, 100)
m_psu = ctrl.Antecedent(r_psu, 'PSU')
m_psu['low'] = fuzz.trimf(r_psu, [-psu_lim, -psu_lim, 0])
m_psu['high'] = fuzz.trimf(r_psu, [0, psu_lim, psu_lim])
m_psu['stable'] = fuzz.trimf(r_psu, [-psu_lim, 0, psu_lim])


# ------------------------------------------------------
# Rules
# creating rules...
rule1 = ctrl.Rule(m_psu['low'], m_pr_d['decrease'])
rule2 = ctrl.Rule(m_psu['high'], m_pr_d['increase'])
rule3 = ctrl.Rule(m_psu['stable'], m_pr_d['nochange'])

fc_psu = FuzzyController([rule1, rule2, rule3], 'PSU', 'PR_delta')
# ------------------------------------------------------


if __name__ == '__main__':

    import matplotlib.pyplot as plt
    m_psu.view()
    m_pr_d.view()
    plt.show()