"""
Script to solve series of equations in a story like manner
General idea of input parameters, equations and present in easy to follow fashion
Simplified idea of Eqwiki website
"""

# necessary imports
from EQScripting.EqClass import *

# ------------------------------------------------------------------
# Equation 1
# Variables
cooling_vardict = {
    "Q": 15000 * units.joules,
    "dT": 10 * units.kelvin,
    "C": 4.186 * units.joules/(units.gram * units.kelvin)
}
target_units = units.kilogram


# Create eqn object
cooling_eq = "Q = M * C * dT"
C_eq = Eqn(cooling_eq)

# Answers
m = C_eq.solve(cooling_vardict, target_units=target_units)


# END
