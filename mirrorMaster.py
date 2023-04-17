import PySimpleGUI as sg
import subprocess
import os
import backloggdMirror as b
import letterboxdMirror as l
import goodreads as g

import json

from saveicon import icon


#https://letterboxd.com/gamegear/rss/
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Click a button to make a mirror')],
            [sg.Text('Backloggd Username:'),sg.InputText(key='backloggd'),sg.Button('Update Backloggd')],
            [sg.Text('Letterboxd Username:'),sg.InputText(key='letterboxd'),sg.Button('Update Letterboxd')],
            [sg.Text('Goodreads Profile Link:'),sg.InputText(key='goodreads'),sg.Button('Update Goodreads')],
            [sg.Button('',image_data=icon, key='Save Config'),sg.Button('Exit'),sg.Button('Upload',key='NeoUp')]]

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
  window['goodreads'].update(config['goodreads'])
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
    elif event=='Update Goodreads':
          #subprocess.call(["python", "letterboxdMirror.py"])
          g.goodReadsUpdate(values['goodreads'])
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