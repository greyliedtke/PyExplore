"""
script for creating simple python workflows
"""


import PySimpleGUI as sg
 

layout = [[sg.Text('Name', size =(15, 1)), sg.InputText("Grey", key="Name")],
        [sg.Submit(), sg.Cancel()]]

def prompt_name():
    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()
    print(event, values)

def tasker():
    window = sg.Window('Simple data entry window', [[sg.Submit()]])
    running = True
    while running:
        event, values = window.read(500)
        if event != "__TIMEOUT__":
            print(event)
            running = False


prompt_name()
tasker()
print("done")