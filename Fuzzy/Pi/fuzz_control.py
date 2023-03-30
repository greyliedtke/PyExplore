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
th1['Right Leaning'] = fuzz.trimf(th1_range, [-90, -90, 0])# fuzz.sigmoid(th1_range, 180, 2)
th1['Balanced'] = fuzz.trimf(th1_range, [-70, 0, 70])# fuzz.sigmoid(th1_range, 180, 2)
th1['Left Leaning'] = fuzz.trimf(th1_range, [0, 90, 90])

# theta rotation
# th1_d['RR'] = fuzz.gaussmf(th1_d_range, -5, 1.5)
# th1_d['LR'] = fuzz.gaussmf(th1_d_range, 5, 1.5)


servo_range = np.arange(0, 181, 1)
servo = ctrl.Consequent(servo_range, 'servo')

servo['theta_cmd_right'] = fuzz.trimf(servo_range, [0, 0, 75])
servo['theta_cmd_left'] = fuzz.trimf(servo_range, [105, 180, 180])
servo['theta_cmd_middle'] = fuzz.gaussmf(servo_range, 90, 30)



# -----------------------------------------------------------------------------------
# creating rules and control system
rule1 = ctrl.Rule(th1['Right Leaning'], servo['theta_cmd_right'])
rule2 = ctrl.Rule(th1['Left Leaning'], servo['theta_cmd_left'])
rule3 = ctrl.Rule(th1['Balanced'], servo['theta_cmd_middle'])
servo_rules = ctrl.ControlSystem([rule1, rule2, rule3])
servo_control = ctrl.ControlSystemSimulation(servo_rules)


def servo_reponse(theta_input):
    servo_control.input['th1'] = theta_input
    servo_control.compute()
    servo_send_angle = servo_control.output['servo']
    return servo_send_angle