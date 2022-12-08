import subprocess
import sys
import PySimpleGUI as sg

# Window Color Pallet
sg.theme('Dark Blue 3')
layout = [[sg.Text('Export users in AD:'), sg.Button('Export')],
          [sg.Text('Export Office 365 Mailboxes:'), sg.Button('Run')],
          [sg.Text('Export Office 365 OneDrive data:'), sg.Button('Run')],
          [sg.Output(size=(60, 20))],  # Progress output for commands
          [sg.Button('Close')]
          ]

# Create the Window
window = sg.Window('Power Python', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

    if event == 'Export':

        break
window.close()

# PowerShell subprocesses
expAD = subprocess.check_output("")
exptMB = subprocess.check_output("")
expOD = subprocess.check_output("")