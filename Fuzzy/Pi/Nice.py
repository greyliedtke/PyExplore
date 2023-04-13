from nicegui import ui
import json
from fuzz_control import motor_fuzz
real=False
if real:
    from motor import motor_cmd
    from mpu_6050 import read_theta

motor = {
    "dir": 0,
    "speed": 0
 }

def send_motor():
    if motor_speed_slider.value<0: motor["dir"]=-1
    elif motor_speed_slider.value>0: motor["dir"]=1
    else: motor["dir"]=0

    motor_dir.value = motor["dir"]
    motor["speed"] = abs(motor_speed_slider.value)
    motor_speed.value = motor["speed"]

    if real:
        motor_cmd(motor["dir"], float(motor["speed"]/100))

def read_acc():
    if real:
        th,thd = read_theta()
    else:
        th,thd = sim_theta_slider.value, sim_theta_slider.value
    theta_x.value = round(th, 1)
    theta_x_dot.value = round(thd, 1)

def control_loop():
    
    if control_mode.value == 'Manual':
        pass
    
    elif control_mode.value == 'Fuzzy':
        # get acc value
        # decide on motor output based off reading
        motor_speed_slider.value = motor_fuzz(theta_x.value)
    
    send_motor()

def stop_motor():
    motor_speed_slider.value = 0
    send_motor()

# UI
ui.markdown("## Pendulum Control")

# ---------------------------------------------------
with ui.row():

    with ui.card():
        control_mode = ui.toggle(['Manual', 'Fuzzy'], value='Manual')
    with ui.card().classes('w-full'):
        ui.timer(interval=0.5, callback=read_acc)
        ui.timer(interval=0.5, callback=control_loop)
        ui.markdown("### Accelerometer")
        theta_x = ui.number("theta")
        theta_x_dot = ui.number("theta_dot")

        sim_theta_slider = ui.slider(min=-45, max=45, value=0)


    with ui.card().classes('w-full'):
        ui.markdown("### Motor")
        motor_dir = ui.number("dir")
        motor_speed = ui.number("%")
        ui.button('OFF', on_click=lambda: stop_motor())
        motor_speed_slider = ui.slider(min=-100, max=100, value=0, on_change=lambda: send_motor())


# running the page
ui.run(title="Pendulum", port=2999, binding_refresh_interval=0.5)
