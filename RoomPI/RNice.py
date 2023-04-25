"""
contorl lights and more eventually...
"""

from nicegui import ui
from RNeo import set_color

real=False
if real:
    pass

lights = {
    "brightness": 0,
    "color": 0
 }


def send_color(cp):
    hex_color = cp.color
    color_button.style(f"background-color:{hex_color}")
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    print(r, g, b)
    set_color(r,g,b)



# UI
ui.markdown("## Color Control")

# ---------------------------------------------------
with ui.row():

    with ui.card():
        control_mode = ui.toggle(['Off', 'On', 'Timer'], value='Off')
    with ui.card().classes('w-full'):
        ui.label('Brightness')
        brightness_slider = ui.slider(min=0, max=100, value=0)


    with ui.card().classes('w-full'):
        ui.markdown("### Color Picker")
        picker = ui.color_picker(on_pick=lambda e: send_color(e))
        color_button = ui.button(on_click=picker.open).props('icon=colorize')

    # send
    ui.button("Send to colors", on_click=lambda:send_color())



# running the page
ui.run(title="RoomPi", port=2999, binding_refresh_interval=0.5)
