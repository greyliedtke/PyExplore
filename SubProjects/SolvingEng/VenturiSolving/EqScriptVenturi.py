"""
Script to solve series of equations in a story like manner
General idea of input parameters, equations and present in easy to follow fashion
Simplified idea of Eqwiki website
"""


# necessary imports
import sympy.physics.units as units
import math


# calculation functions ------------------------------------------------------------------------------------------------
def diam_to_area(diam):
    area = math.pi * diam**2 / 4
    return area


def dp_to_cfm(dp, a1, a2, rho):
    flow = a1 * ((2 / rho) * (dp / ((a1 / a2) ** 2 - 1))) ** .5

    # converting to ft^3 / min
    flow = units.convert_to(flow, units.feet ** 3 / units.minute)
    return flow


def isentropic_flow(neck_d, upstream_d, p2, p1, rho_1):
    # unsure of this calculation...
    c_d = .985          # cause re at throat is 4e5???
    beta = neck_d / upstream_d
    tau = p2 / p1
    k = 1.4
    # expansion factor. Unsure where this came from...
    eta = ((k * tau**(2/k) / (k-1)) * ((1-beta**4) / (1 - beta**4 * tau ** (2/k))) * ((1 - tau ** ((k-1)/k)) / (1-tau))) ** -.5
    q_m = (c_d / (1 - beta)**4) * eta * (math.pi * neck_d**2 / 4) * (2 * (p1 - p2)/rho_1)**.5
    q_m = units.convert_to(q_m, units.feet ** 3 / units.minute)
    return q_m
# ----------------------------------------------------------------------------------------------------------------------


# venturi_dimensions
venturi_in_id = 2.067 * units.inch
venturi_in_area = diam_to_area(venturi_in_id)
venturi_throat_id = 1.2 * units.inch
venturi_throat_area = diam_to_area(venturi_throat_id)

# bellmouth dimensions
bm_in_id = 10.9 * units.inch
bm_in_area = diam_to_area(bm_in_id)
bm_throat_id = 5.45 * units.inch
bm_throat_area = diam_to_area(bm_throat_id)

# air conditions
rho_air = 1.225 * units.kg / units.meter**3

# data collection
venturi_dp_1 = 7750 * units.pascals
venturi_flow_1 = dp_to_cfm(venturi_dp_1, venturi_in_area, venturi_throat_area, rho_air)
venturi_dp_2 = 11500 * units.pascals
venturi_flow_2 = dp_to_cfm(venturi_dp_2, venturi_in_area, venturi_throat_area, rho_air)

bm_dp_1 = .15 * 248.84 * units.pascals  # in h20 to pa measurement
bm_flow_1 = dp_to_cfm(bm_dp_1, bm_in_area, bm_throat_area, rho_air)
bm_dp_2 = .21 * 248.84 * units.pascals  # in h20 to pa measurement
bm_flow_2 = dp_to_cfm(bm_dp_2, bm_in_area, bm_throat_area, rho_air)


print(f"Venturi Flow_1: {venturi_flow_1}")
print(f"Bellmouth Flow_1: {bm_flow_1}")
print(f"Venturi Flow_2: {venturi_flow_2}")
print(f"Bellmouth Flow_2: {bm_flow_2}")

# END
