"""
creating fuzzy controller for PR and fuel control
"""
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
from FuzzyClass import FuzzyController, generic_member

# ------------------------------------------------------
# Th Error
m_n2_error= generic_member("n2_err", 2)
m_n2_acc = generic_member("n2_acc", .5)
m_pr_delta = generic_member("PR_delta", .2)
pr_adj = generic_member("pr_adj", .2, consequent=True)

# ------------------------------------------------------
# Rules
# creating rules...
rule1 = ctrl.Rule(m_n2_error['low'] & m_n2_acc['low'], pr_adj['high'])
rule2 = ctrl.Rule(m_n2_error['high'] & m_n2_acc['high'], pr_adj['low'])
rule3 = ctrl.Rule(m_pr_delta['high'] & m_n2_acc['high'], pr_adj['low'])
rule4 = ctrl.Rule(m_n2_error['stable'] & m_n2_acc['stable'], pr_adj['stable'])
rule5 = ctrl.Rule(m_pr_delta['low'] & m_n2_acc['low'], pr_adj['high'])

fc_vb = FuzzyController([rule1, rule2, rule3, rule4, rule5], ['n2_err', 'n2_acc', 'PR_delta'], 'pr_adj')
# ------------------------------------------------------