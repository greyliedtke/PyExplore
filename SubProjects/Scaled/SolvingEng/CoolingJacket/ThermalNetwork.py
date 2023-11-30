""" Script to Predict temperatures of cooling jacket """
from CoolingLoopEQ import *


# defined from thermal network:
v = 1.06
r = u('.006 ohm')


# generator max conditions constraints
# winding max: 155, rotor 150 c
speed_max = 40000
q_max = u('80 kW')
v_rms_max = u(f"{speed_max * 2.54 * v} volts")
efficiency = .96
t_winding = u('428 K')
t_stator = t_winding - u('5 K')
t_wall = u('300 K')


# loss calculations
total_loss = q_max * (1-efficiency)
winding_loss = r * 3 * (1000*q_max/(3*v_rms_max))**2
winding_loss = winding_loss.to_compact('kW')
lamination_loss = total_loss - winding_loss
print("losses", total_loss, winding_loss, lamination_loss)

# equivalent resistance
# q = dt / r
r_eq_tot = (t_stator - t_wall)/total_loss
r_eq_wind = (t_winding - t_stator)/winding_loss
r_eq_stat = r_eq_tot - r_eq_wind
print("r_equiv:", r_eq_tot, r_eq_wind, r_eq_stat)

# running under experimental conditions:
# using 30 kW at 40 krpm
speed = u("40000 turn/min")
power_level = u('30 kW')
exp_eff = .962
# v_rms = speed * 2.54 * v
v_rms_exp = u("107.696 volts")

# experimental losses
loss_exp = power_level * (1-exp_eff)
winding_loss_exp = r * 3 * (power_level/(3*v_rms_exp))**2
winding_loss_exp = winding_loss_exp.to_compact('kW')
lamination_loss = loss_exp - winding_loss_exp

t_wall_exp = t_winding - loss_exp*r_eq_tot
t_stator_exp = t_winding - winding_loss_exp*r_eq_wind
print("wall temps:", t_wall_exp, t_stator_exp)

# assume delta T of 20 K
deltaT_h = u("20 K")
t_avg = t_wall_exp - deltaT_h
t_oil_cels = t_avg - u('273.15 K')
print("Oil avg temp celsius:", t_oil_cels)
# end of script
