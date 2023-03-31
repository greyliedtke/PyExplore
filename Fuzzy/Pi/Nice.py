from nicegui import ui
import json
from motor import motor_cmd
from mpu_6050 import read_theta

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
    motor_cmd(motor["dir"], float(motor["speed"]/100))

def read_acc():
    th,thd = read_theta()
    theta_x.value = round(th, 1)
    theta_x_dot.value = round(thd, 1)


# UI
ui.markdown("## Pendulum Control")

# ---------------------------------------------------
with ui.row():
    with ui.card() as card:
        card.classes('w-full')
        ui.timer(interval=0.5, callback=read_acc)
        ui.markdown("### Accelerometer")
        theta_x = ui.number("theta")
        theta_x_dot = ui.number("theta_dot")

    with ui.card() as card:
        ui.markdown("### Motor")

        dir_toggle = ui.toggle(['OFF','FWD', 'BWD'], on_change=lambda: send_motor())
        motor_speed_slider = ui.slider(min=0, max=100, value=0, on_change=lambda: send_motor())


# running the page
ui.run(title="Pendulum", port=2999, binding_refresh_interval=0.5)
