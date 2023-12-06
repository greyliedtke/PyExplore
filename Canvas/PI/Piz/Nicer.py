"""
contorl lights and more eventually...
sine wave
random bursts
primary_color
secondary_color
"""

from nicegui import ui
from datetime import datetime

pi = True
if pi:
    import canvas_clock as cc
    from sine import send_sine
    from hombre import send_hombre

def timer_loop():
    if mode.value == "Clock":
        if pi: cc.clock_set()
    elif mode.value == "Sine":
        ts = datetime.now().second*tst.value
        if pi: send_sine(amp.value, freq.value, ts)
    elif mode.value == "Hombre":
        if pi: send_hombre(c1.value, c2.value)

tt = ui.timer(.20, lambda: timer_loop())

with ui.card():
    ui.markdown("## Clock Control")
    mode = ui.toggle(
        ["Clock", "Sine", "Hombre"], value="Clock", on_change=lambda value: print(value)
    )
    ng_bright = ui.number("Brightness", value=3)

with ui.card():
    c1 =  ui.color_input(label="Color", value="#ff0000")
    c2 =  ui.color_input(label="Color", value="#ff0000")
    ui.button("Set Color", on_click=lambda: print("Set Color"))

with ui.expansion("Sine"):
    amp = ui.number("Amplitude", value=7)
    freq = ui.number("Frequency", value=.5)
    tst = ui.number("Time Step", value=.25)
    
# running the page
ui.run(title="PiControl", port=3000, binding_refresh_interval=0.5)
