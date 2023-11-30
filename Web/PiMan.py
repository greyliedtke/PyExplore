"""
contorl lights and more eventually...
"""

from nicegui import ui
from datetime import datetime

real=False
if real:
    pass

def time_display():
    tn =  datetime.now()
    t_date = tn.strftime("%A %m/%d")
    ui.markdown(f"### {t_date}")
    time_now = ui.markdown()
    ui.timer(1.0, lambda: time_now.set_content(f'### {datetime.now():%X}'))

with ui.card():
    ui.markdown("### Color Control")
    def led_new(color, strip):
        if strip == 1:
            b_color_1.style(f'background-color:{color}!important')
            print(color)
            print(strip_1_slider.value)
        elif strip == 2:
            b_color_2.style(f'background-color:{color}!important')

    with ui.row():
        with ui.button(text="Strip1", icon='colorize') as b_color_1:
            def on_color_pick1(e):
                led_new(e.color, 1)
            s1 = ui.color_picker(on_pick=on_color_pick1)
            strip_1_slider = ui.slider(min=0, max=100, value=10)

        with ui.button(text="Strip2", icon='colorize') as b_color_2:
            def on_color_pick2(f):
                led_new(f.color, 2)
            ui.color_picker(on_pick=on_color_pick2)
            strip_2_slider = ui.slider(min=0, max=100, value=10)


# HEADER
with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
    with ui.row():
        time_display()
    ui.label('PiController')

    ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

# RIGHT SIDE
with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
    ui.link("Note Form", "https://www.google.com/")



# running the page
ui.run(title="PiControl", port=2999, binding_refresh_interval=0.5)


"""
ui.notify("Created file ...")

ui.button("collect data", on_click=lambda:collect_data())
ui.label("Hold q to stop")

ui.run(title="DispSensor", port=2999, binding_refresh_interval=0.5)

"""
