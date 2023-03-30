from nicegui import ui
import json
from Pi.motor import motor_cmd

motor = {
    "dir": 0,
    "speed": 0
 }

def funcer(angle):
    print(f'servo angle:{angle}')
    pass

def send_motor():
    motor["dir"] = dir_toggle.value
    motor["speed"] = motor_speed_slider.value

def read_acc():
    print('reading acc')


# UI
ui.markdown("## Pendulum Control")

# ---------------------------------------------------
with ui.row():
    with ui.card() as card:
        ui.timer(interval=0.5, callback=read_acc)
        ui.markdown("### Accelerometer")

        theta_x = ui.number("theta")
        theta_x_dot = ui.number("theta_dot")

    with ui.card() as card:
        ui.markdown("### Motor")

        dir_toggle = ui.toggle(['OFF','FWD', 'BWD'], on_change=lambda: send_motor())
        motor_speed_slider = ui.slider(min=0, max=100, value=90, on_change=lambda: send_motor())


# running the page
ui.run(title="Pendulum", port=2999, binding_refresh_interval=0.5)
