import PySimpleGUI as sg
import subprocess
import os

#https://letterboxd.com/gamegear/rss/
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Click a button to make a mirror')],
            [sg.Button('Update Backloggd')],
            [sg.Button('Update Letterboxd')],
            [sg.Button('NeoUp')],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ',str(event))
    if event=='Update Backloggd':
          subprocess.call(["python", "backloggdMirror.py"])
    elif event=='Update Letterboxd':
          subprocess.call(["python", "letterboxdMirror.py"])
    elif event=='NeoUp':
          os.system("update")

          

window.close()
