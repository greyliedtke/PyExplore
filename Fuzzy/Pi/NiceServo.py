from nicegui import ui
import json
from fuzz_control import motor_fuzz
from servo import send_servo_angle, servo_sweep

# real=False
# if real:
#     from motor import motor_cmd

def send_servo():
    print(slider_servo.value)
    send_servo_angle(slider_servo.value)


def control_loop():
    
    if control_mode.value == 'Manual':
        pass
    
    elif control_mode.value == 'Fuzzy':
        pass
        # get acc value
        # decide on motor output based off reading
        # motor_speed_slider.value = motor_fuzz(theta_x.value)
    
    # send_motor()


# UI
ui.markdown("## Servo Control")

# ---------------------------------------------------
with ui.row():

    with ui.card():
        control_mode = ui.toggle(['Manual', 'Fuzzy'], value='Manual')
    with ui.card().classes('w-full'):
        # ui.timer(interval=0.5, callback=read_acc)
        ui.timer(interval=0.5, callback=control_loop)
        ui.markdown("### Accelerometer")
        theta_x = ui.number("theta")
        theta_x_dot = ui.number("theta_dot")

        sim_theta_slider = ui.slider(min=-45, max=45, value=0)


    with ui.card().classes('w-full'):
        ui.markdown("### Servo")
        ui.button("servosweep", on_click=lambda: servo_sweep())
        
        motor_dir = ui.number("dir")
        motor_speed = ui.number("%")
        slider_servo = ui.slider(min=0, max=180, value=90, on_change=lambda: send_servo())


# running the page
ui.run(title="Pendulum", port=2999, binding_refresh_interval=0.1)
