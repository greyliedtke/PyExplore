"""
creating fuzzy controller for PR and fuel control
"""
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
from FuzzyClass import FuzzyController, generic_member

# ------------------------------------------------------
# Th Error
m_theta = generic_member("Theta_Error", 18)
m_servo = generic_member("Servo_Response", 20, consequent=True)

# ------------------------------------------------------
# Rules
# creating rules...
rule1 = ctrl.Rule(m_theta['low'], m_servo['high'])
rule2 = ctrl.Rule(m_theta['high'], m_servo['low'])
rule3 = ctrl.Rule(m_theta['stable'], m_servo['stable'])

fc_theta = FuzzyController([rule1, rule2, rule3], 'Theta_Error', 'Servo_Response')
# ------------------------------------------------------