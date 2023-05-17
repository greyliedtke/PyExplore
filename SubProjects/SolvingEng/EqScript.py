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

# ------------------------------------------------------------------
# Equation 2
# Variables
dens_dict = {
    "m": m,
    "V": 10 * units.liters
}
d_target_units = units.kilogram / units.meter**3

# Create eqn object
dens_eq = "rho = m / V"
d_eq = Eqn(dens_eq)
rho = d_eq.solve(dens_dict, target_units=d_target_units)


# ------------------------------------------------------------------
# iterating example
rhos = []
for v in range(1, 10):
    dens_dict = {
        "m": m,
        "V": v * units.liters
    }
    d = d_eq.solve(dens_dict, target_units=d_target_units, p_story=False)

    # get tuple of answer and just selecting value
    rhos.append(d.as_coeff_Mul()[0])


# END
