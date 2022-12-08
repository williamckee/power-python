import subprocess
import sys
import PySimpleGUI as sg

sg.theme('Dark Blue 3')
layout = [
    [sg.Combo(['Export AD Users', 'Export O365 Mailbox Data', 'Export OneDrive Data'], size=(60, 20),
              enable_events=True,key='selected')],
    [sg.Output(size=(60, 20))],  # Progress output for commands
    [sg.Button('Reload'),sg.Button('Run'), sg.Button('Close')]
]

# Create the Window
window = sg.Window('Power Python', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break

    if event == 'Reload':
        print('Getting scripts...')
        window.refresh()

    if event == 'Run':
        item = values['selected']
        print(item + '...')
window.close()
