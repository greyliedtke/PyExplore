"""
file to control fuzzy logic setup
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# -----------------------------------------------------------------------------------
# membership function for theta
th1_range = np.arange(-90, 91, 1)
th1 = ctrl.Antecedent(th1_range, 'th1')


# Auto-membership function population is possible with .automf(3, 5, or 7)
# accelerometer memberships
# theta leaning
th1['Right Leaning'] = fuzz.trimf(th1_range, [-45, -45, 0])# fuzz.sigmoid(th1_range, 180, 2)
th1['Balanced'] = fuzz.trimf(th1_range, [-30, 0, 30])# fuzz.sigmoid(th1_range, 180, 2)
th1['Left Leaning'] = fuzz.trimf(th1_range, [0, 45, 45])

# theta rotation
# th1_d['RR'] = fuzz.gaussmf(th1_d_range, -5, 1.5)
# th1_d['LR'] = fuzz.gaussmf(th1_d_range, 5, 1.5)

motor_range = np.arange(-100, 100, 1)
motor = ctrl.Consequent(motor_range, 'motor')

motor['theta_cmd_right'] = fuzz.trimf(motor_range, [-100, -100, 0])
motor['theta_cmd_left'] = fuzz.trimf(motor_range, [0, 100, 100])
motor['theta_cmd_middle'] = fuzz.gaussmf(motor_range, 0, 30)



# -----------------------------------------------------------------------------------
# creating rules and control system
rule1 = ctrl.Rule(th1['Right Leaning'], motor['theta_cmd_right'])
rule2 = ctrl.Rule(th1['Left Leaning'], motor['theta_cmd_left'])
rule3 = ctrl.Rule(th1['Balanced'], motor['theta_cmd_middle'])
motor_rules = ctrl.ControlSystem([rule1, rule2, rule3])
motor_control = ctrl.ControlSystemSimulation(motor_rules)


def motor_fuzz(theta_input):
    motor_control.input['th1'] = theta_input
    motor_control.compute()
    motor_signal = motor_control.output['motor']
    return motor_signal