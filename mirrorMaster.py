import PySimpleGUI as sg
import subprocess
import os
import backloggdMirror as b
import letterboxdMirror as l

import json



#https://letterboxd.com/gamegear/rss/
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Click a button to make a mirror')],
            [sg.Text('Backloggd Username:'),sg.InputText(key='backloggd'),sg.Button('Update Backloggd')],
            [sg.Text('Letterboxd Username:'),sg.InputText(key='letterboxd'),sg.Button('Update Letterboxd')],
            [sg.Button('NeoUp'),sg.Button('Save Config'),sg.Button('Exit')]]

# Create the Window
window = sg.Window('Window Title', layout,finalize = True)
# Event Loop to process "events" and get the "values" of the inputs


if os.path.exists('config.json'):
  fyle = open('config.json','r')
  fig = fyle.read()
  fyle.close()
  config = json.loads(fig)
  print(config['backloggd'])
  window['backloggd'].update(config['backloggd'])
  window['letterboxd'].update(config['letterboxd'])
  first = True
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event=='Update Backloggd':
          #subprocess.call(["python", "backloggdMirror.py"])
          b.backloggdUpdate(values['backloggd'])
    elif event=='Update Letterboxd':
          #subprocess.call(["python", "letterboxdMirror.py"])
          l.letterboxdUpdate(values['letterboxd'])
    elif event=='NeoUp':
          os.system("upload.bat")
    elif event=='Save Config':
          js = json.dumps(values)
          fyle = open('config.json','w')
          fyle.write(js)
          fyle.close()
    else:
      print(event)
          

          

window.close()