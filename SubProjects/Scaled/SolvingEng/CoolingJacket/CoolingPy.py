""" Script to recalculate all fluid values for ones featured in CoolingCSV"""
import pandas as pd
from CoolingLoopEQ import *


# Create dataframe for project parameters
df_param = pd.read_csv("InputParameters.csv")

# parameters read from setup csv
vol_flow = u(df_param.iloc[0]["Volumetric Flow"])
ch_width = u(df_param.iloc[0]["Channel Width"])
ch_height = u(df_param.iloc[0]["Channel Height"])
ch_revs = df_param.iloc[0]["Channel Revs"]
ch_path_diam = u(df_param.iloc[0]["Channel Path Diameter"])
load = u(df_param.iloc[0]["Load"])

# Calculated from problem setup
diam_hyd = rect_hyd_diam(ch_width, ch_height)     # hydraulic diameter of channel
channel_ca = ch_width*ch_height
contact_length = math.pi*ch_revs*ch_path_diam
channel_sa = (2*ch_width + 2*ch_height) * contact_length  # surface area of all 4 sides of channel
vel = vol_flow/channel_ca

# Problem Parameters Output
df_param.at[0, "Hydraulic Diameter"] = str(diam_hyd)
df_param.at[0, "Cross Sectional Area"] = str(channel_ca)
df_param.at[0, "Contact Length"] = str(contact_length)
df_param.at[0, "Surface Area"] = str(channel_sa)
df_param.at[0, "Velocity"] = str(vel.to_compact("m/s"))
df_param.to_csv("ParametersOutput1.csv")


# create dataframes to work with inputs
df_prop = pd.read_csv("InputProperties.csv")

# loop through entries in the input file
for fluid_i in range(len(df_prop)):
    # read in properties from fluid
    fluid = df_prop.iloc[fluid_i]["Fluid"]
    density = u(df_prop.iloc[fluid_i]["Density"])
    cp = u(df_prop.iloc[fluid_i]["cp"])
    viscosity = u(df_prop.iloc[fluid_i]["Viscosity"])
    conductivity = u(df_prop.iloc[fluid_i]["Conductivity"])

    # class that calculates dimensionless numbers and coefficients
    correlations = FluidNumbers(density, vel, diam_hyd, viscosity, cp, conductivity, show=True)

    # inputing correlation back into dataframe to save to output file
    df_prop.at[fluid_i, "Re"] = correlations.re
    df_prop.at[fluid_i, "Pr"] = correlations.pr
    df_prop.at[fluid_i, "Nu"] = correlations.nu
    dean = correlations.re*(diam_hyd/ch_path_diam)**.5
    df_prop.at[fluid_i, "Dean"] = dean
    df_prop.at[fluid_i, "Nu_dean"] = .76 * correlations.re**(-.23) * dean**(-.114)
    df_prop.at[fluid_i, "Fr"] = correlations.fric_factor
    df_prop.at[fluid_i, "H_factor"] = str(correlations.h)
    df_prop.at[fluid_i, "DeltaT"] = temps_from_q_load(load, correlations, channel_sa)
    df_prop.at[fluid_i, "Necessary Area"] = necessary_area(load, correlations, u("30 K"))
    df_prop.at[fluid_i, "PressureDrop"] = str(Loss.major(correlations.fric_factor, contact_length, vel, diam_hyd,
                                                         density))
    df_prop.at[fluid_i, "Q_20"] = str((correlations.h*channel_sa*u("20 K")).to_compact("kW"))

print("Necesary Area:", df_prop.iloc[1]["Necessary Area"])
print("Pressure Drop:", df_prop.iloc[1]["PressureDrop"])
print("Surface Area", df_param.iloc[0]["Surface Area"])

# save dataframe as csv output
df_prop.to_csv("Output1.csv")

# end of script

