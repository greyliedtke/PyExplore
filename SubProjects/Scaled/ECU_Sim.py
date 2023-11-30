"""
Creating simulation for engine control

- PID
- Load following
- Time

"""

from nicegui import ui
from datetime import datetime


with ui.card():
    ui.markdown("### Simulated Values")
    with ui.row():
        n2_speed = ui.number("N2 Speed", value=16)
        fuel_pressure = ui.number("Fuel Pressure", value=0)
        power = ui.number("Power", value=0)

with ui.card():
    ui.markdown("### Control")
    with ui.row():
        fuel_output = ui.number("Fuel Signal", value=0)
        cmd = ui.radio(["OFF", "STANDBYE", "LIGHTOFF", "IDLE", "LOAD", "COOLDOWN"])

# HEADER
with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
    ui.label('Simulator')

def control_loop():
    sim_dict = {
        "N2":n2_speed.value,
        "Fuel Pressure":fuel_pressure.value,
        "Power":power.value
    }
    # post to redis...


ui.timer(.5, lambda: control_loop())

# running the page
ui.run(title="PiSim", port=2999, binding_refresh_interval=0.5)
