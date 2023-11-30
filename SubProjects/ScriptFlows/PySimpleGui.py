"""
script for creating simple python workflows
"""



layout = [[sg.Text('Name', size =(15, 1)), sg.InputText("Grey", key="Name")],
        [sg.Submit(), sg.Cancel()]]

import PySimpleGUI as sg
 
def prompt():
    window = sg.Window('RUN NI', [[sg.Submit("START")]])
    event, values = window.read()
    window.close()

def run_ni():
    window = sg.Window('Collecting Data', [[sg.Submit("STOP")]])
    running = True
    while running:
        event, values = window.read(250)
        if event != "__TIMEOUT__":
            print(event)
            running = False
        print("Loop")


prompt()
run_ni()
print("done")