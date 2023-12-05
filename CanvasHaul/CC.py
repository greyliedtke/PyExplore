"""
contorl lights and more eventually...
"""

from nicegui import ui
from datetime import datetime
import time

pi = True
if pi:
    time.sleep(30)
    import canvas_clock as cc

def timer_loop():
    if mode.value == "Clock":
        if pi: cc.clock_set()

tt = ui.timer(1.0, lambda: timer_loop())

with ui.card():
    ui.markdown("## Clock Control")
    mode = ui.toggle(
        ["Clock", "Timer", "Art"], value="Clock", on_change=lambda value: print(value)
    )
    ng_bright = ui.number("Brightness", value=3)

with ui.card():
    clock_color =  ui.color_input(label="Color", value="#ff0000")
    outline_color =  ui.color_input(label="Color", value="#ff0000")
    ui.button("Set Color", on_click=lambda: print("Set Color"))


with ui.expansion("Art"):
    c1 = ui.color_input(label="Color", value="#ff0000")
    c2 = ui.color_input(label="Color", value="#ff0000")
    ui.button("Set Color", on_click=lambda: print("Set Color"))


# running the page
ui.run(title="PiControl", port=3000, binding_refresh_interval=0.5)
