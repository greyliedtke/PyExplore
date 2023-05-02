from nicegui import ui
import json
from datetime import datetime

v_dict = {
    'fuel_percent':0,
    'fuel_psi':0,
    'fuel_gph':0,
    'load_level':0,
    'phase_r':0,
    'n1':0,
    'n2':0,
    'pr':0,
    't_turbine_exit':0,
    'voltage':0,
    'current':0,
    'power':0
}


def sys_update():
    v_dict['fuel_percent'] = fuel_slider.value
    v_dict['fuel_psi'] = round(v_dict['fuel_percent']*2.1,1)
    v_dict['fuel_gph'] = round(v_dict['fuel_percent']*.1,2)
    fuel_percent.value = v_dict['fuel_percent']
    fuel_pressure.value = v_dict['fuel_psi']
    fuel_flowrate.value = v_dict['fuel_gph']

    # load level
    v_dict['load_level']= load_slider.value
    load_level.value = v_dict['load_level']
    v_dict['phase_r'] = 10/v_dict['load_level']
    phase_r.value = round(v_dict['phase_r'],2)

    # speed setting
    v_dict['n1']=round(v_dict['fuel_percent']*1.4,1)
    v_dict['n2'] = v_dict['n1']/3*(140/(v_dict['load_level']*4+100))
    n1.value=round(v_dict['n1'],1)
    n2.value=round(v_dict['n2'],1)

    # engine
    v_dict['pr'] = round(n1.value/140*4,1)
    pr.value = v_dict['pr']
    v_dict['t_turbine_exit'] = 600+v_dict['fuel_percent']
    turbine_exit.value = v_dict['t_turbine_exit'] 
    # power measurement
    v_dict['voltage'] = round(v_dict['n2']*3.48,1)
    voltage.value = v_dict['voltage']
    v_dict['current'] = round(voltage.value/v_dict['phase_r'],1)
    current.value = v_dict['current']
    v_dict['power'] = round(voltage.value*current.value*3/1000,1)

# ---------------------------------------------------
with ui.row():
    with ui.card() as card:
        ui.markdown("### Fuel Input")
        fuel_slider = ui.slider(min=0, max=100, value=0, on_change=lambda: sys_update())
        with ui.row():
            fuel_percent = ui.number('Fuel %:')
            fuel_pressure = ui.number('Fuel Pressure%:')
            fuel_flowrate = ui.number('Fuel GPH:')

    with ui.card() as card:
        ui.markdown("### Load Setting")

        load_slider = ui.slider(min=1, max=10, value=1, on_change=lambda: sys_update())
        with ui.row():
            load_level = ui.number('Load Level')
            phase_r = ui.number('Phase Resistance')

    with ui.card() as card:
        ui.markdown("### Engine")
        with ui.row():
            pr = ui.number('Pressure Ratio')
            turbine_exit = ui.number('Turbine Exit')
        ui.markdown("### Speeds")
        with ui.row():
            n1 = ui.number('N1')
            n2 = ui.number('N2')
        ui.markdown("### Power")
        with ui.row():
            voltage = ui.number('Volts')
            current = ui.number('Amps')
            power = ui.number('kW')





# running the page
ui.run(title="TurboSimulator", port=2999, binding_refresh_interval=0.5)
