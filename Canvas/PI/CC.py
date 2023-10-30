"""
contorl lights and more eventually...
"""

from nicegui import ui
from datetime import datetime
from Tools.ClockMat import digits, segments

pizero = True
if pizero:
    import neopixel
    import board
    strip_length = 255
    s1 = neopixel.NeoPixel(board.D12, strip_length, auto_write=False)

# include brightness by rounding...
ng_bright = ui.number("Brightness", value=3)

def time_send(dplace, number):
    # set everything to zero


    p_mat = digits[dplace]  # pixel matrix to loop through
    number_cmd = segments[number]

    for i, row in enumerate(p_mat):
        number_row = number_cmd[i]
        for j, pixel in enumerate(row):
            if number_row[j]:
                if pizero:
                    s1[pixel] = [0,0,10]
                    s1.show()

def clock_setting():
    tn = datetime.now().strftime("%H:%M:%S")

    tc = tn[0], tn[1], tn[3], tn[4]
    for i, t in enumerate(tc):
        time_send(i+1, int(t))


tt = ui.timer(1.0, lambda: clock_setting())

def time_display():
    print("Clock Mode")
    print(int(ng_bright.value))
    tt.activate()

def stop_clock():
    print("stop Mode")
    tt.deactivate()

ui.button("Clock Mode", on_click=lambda:clock_setting())
ui.button("Stop Mode", on_click=lambda:stop_clock())


# running the page
ui.run(title="PiControl", port=3000, binding_refresh_interval=0.5)
