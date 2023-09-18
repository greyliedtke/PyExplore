"""
script for simulating pid stuff
"""

# ------------------------------------------------------
# IMPORTS
from nicegui import ui
from datetime import datetime
import matplotlib.pyplot as plt
from EnginePID import pid_n2

# HEADER
with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
    ui.label('Simulator')

# initialize data
ts = datetime.now()
d_x = [0]
d_y = [0]
d_n2sp = [0]
d_fuel_ao = [0]

def ramp_n2():
    pass


# simulating values
with ui.card():
    ui.markdown("### Simulated Values")
    with ui.row():
        n2_speed = ui.slider(min=0, max=50, value=0)
        ui.label("N2 Speed:")
        ui.label("N2 Speed").bind_text_from(n2_speed, "value")
        
        fuel_ao = ui.slider(min=0, max=100)
        ui.label("Fuel Output")
        n2sp = ui.slider(min=20, max=40, value=24)
        ui.label("N2 Setpoint")

def plot_update(x, y, sp, fuel):
    with ngp:
        plt.clf()
        plt.plot(x, y)
        plt.plot(x, sp)
        plt.ylim([0, 40])

    with ngp2:
        plt.clf()
        plt.plot(x, fuel)
        plt.ylim([0, 100])

def control_loop():

    # update pid setpoint
    pid_n2.pid.setpoint = n2sp.value
    # call loop
    new_ao = pid_n2.loop(n2_speed.value, d_fuel_ao[-1])

    et = (datetime.now() - ts).total_seconds()


    d_x.append(et)
    d_y.append(n2_speed.value)
    d_n2sp.append(n2sp.value)
    d_fuel_ao.append(new_ao)

    d_length = 15

    p_x = d_x[-d_length:]
    p_y = d_y[-d_length:]
    p_sp = d_n2sp[-d_length:]
    p_fuel = d_fuel_ao[-d_length:]
    
    plot_update(p_x, p_y, p_sp, p_fuel)

with ui.row():
    ui.label("N2")
    ui.label("Fuel Output")

with ui.row():
    ngp = ui.pyplot(close=False)
    ngp2 = ui.pyplot(close=False)

ui.timer(.5, lambda: control_loop())
ui.run(title="PID Sim", port=2999, binding_refresh_interval=0.1)
