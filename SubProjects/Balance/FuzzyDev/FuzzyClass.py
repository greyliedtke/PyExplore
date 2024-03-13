"""
file to develop fuzzy logic control system
"""

# imports
from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np

# ------------------------------------------------------
# Controller class for fuzzy logic
class FuzzyController:
    def __init__(self, rules, input, output):
        self.input = input
        self.output = output
        control_rules = ctrl.ControlSystem(rules)
        self.controller = ctrl.ControlSystemSimulation(control_rules)

    def compute(self, inputs):
        self.controller.inputs(inputs)
        # self.controller.inputs[self.input] = inputs
        self.controller.compute()
        output = self.controller.output[self.output]
        return output
# ------------------------------------------------------

def generic_member(desc, s_limit, consequent=False):
    # create generic memebership for function given input range
    s_range = np.linspace(-s_limit, s_limit)
    if consequent: 
        mem = ctrl.Consequent(s_range, desc)
    else:
        mem = ctrl.Antecedent(s_range, desc)
    mem['low'] = fuzz.trimf(s_range, [-s_limit, -s_limit, 0])
    mem['stable'] = fuzz.trimf(s_range, [-s_limit, 0, s_limit])
    mem['high'] = fuzz.trimf(s_range, [0, s_limit, s_limit])
    return mem
