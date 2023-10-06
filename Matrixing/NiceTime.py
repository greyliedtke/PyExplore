"""
contorl lights and more eventually...
"""

from nicegui import ui
from datetime import datetime


# put it all on one clock...
r_numbs = [24, 16, 8]
c_sec = [255, 0, 0]
c_min = [0, 255, 0]
c_hour = [0, 0, 255]

def time_to_pix(time_format):
    t_split = time_format.split(":")
    p_h = round((int(t_split[0])/24)*r_numbs[0])
    p_m = round((int(t_split[1])/60)*r_numbs[1])
    p_s = round((int(t_split[2])/60)*r_numbs[2])
    return p_h, p_m, p_s

def clock_setting():
    tn = datetime.now().strftime("%H:%M:%S")
    pis = time_to_pix(tn)
    print(pis)

tt = ui.timer(1.0, lambda: clock_setting())

def time_display():
    print("Clock Mode")
    tt.activate()

def stop_clock():
    print("stop Mode")
    tt.deactivate()
    



ui.button("Clock Mode", on_click=lambda:time_display())
ui.button("Stop Mode", on_click=lambda:stop_clock())


# running the page
ui.run(title="PiControl", port=2999, binding_refresh_interval=0.5)


"""
ui.notify("Created file ...")

ui.button("collect data", on_click=lambda:collect_data())
ui.label("Hold q to stop")

ui.run(title="DispSensor", port=2999, binding_refresh_interval=0.5)

"""
