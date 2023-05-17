"""
Script to understand how seamus solves for orifice sizing...
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

# ----------------------------------------------------------------------------------------------------------------------


# inlet conditions
i_flowrate = .13 * units.kg / units.s
i_pressure = 192 * units.kPa
i_temperature = 378 * units.kelvin
i_density = 1.76 * units.kg / units.meter**3

# pressure drops
mixer_inlet_pd_p = .0144
mixer_inlet_pd = mixer_inlet_pd_p * i_pressure
swirler_pd_p = .00094
swirler_pd = swirler_pd_p * i_pressure

# bellmouth dimensions
bm_in_id = 10.9 * units.inch
bm_in_area = diam_to_area(bm_in_id)
bm_throat_id = 5.45 * units.inch
bm_throat_area = diam_to_area(bm_throat_id)

# venturi_dimensions
venturi_in_id = 2.067 * units.inch
venturi_in_area = diam_to_area(venturi_in_id)
venturi_throat_id = 1.2 * units.inch
venturi_throat_area = diam_to_area(venturi_throat_id)

# air conditions
rho_air = 1.225 * units.kg / units.meter**3

# venturi data collection and flow calculation
venturi_dp_1 = 7750 * units.pascals
venturi_flow_1 = dp_to_cfm(venturi_dp_1, venturi_in_area, venturi_throat_area, rho_air)
venturi_dp_2 = 11500 * units.pascals
venturi_flow_2 = dp_to_cfm(venturi_dp_2, venturi_in_area, venturi_throat_area, rho_air)


# bm data collection and flow calculation
bm_dp_1 = .15 * 248.84 * units.pascals  # in h20 to pa measurement
bm_flow_1 = dp_to_cfm(bm_dp_1, bm_in_area, bm_throat_area, rho_air)
bm_dp_2 = .21 * 248.84 * units.pascals  # in h20 to pa measurement
bm_flow_2 = dp_to_cfm(bm_dp_2, bm_in_area, bm_throat_area, rho_air)

# print results
print(f"Venturi Flow_1: {venturi_flow_1}")
print(f"Bellmouth Flow_1: {bm_flow_1}")
print(f"Venturi Flow_2: {venturi_flow_2}")
print(f"Bellmouth Flow_2: {bm_flow_2}")

# END
