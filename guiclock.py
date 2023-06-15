import PySimpleGUI as sg
from datetime import datetime
from os import system, name
from time import sleep
import pytz

sg.theme('DarkAmber')

layout = [[sg.Text('The time now: ')],
                [sg.Output(key='-OUTPUT-')],
                [sg.Button('Exit')]]
                
window = sg.Window('GUI Clock on Break', layout, finalize = False)

def clockfunc():
    while True:
	    timeEST = pytz.timezone("America/New_York")
	    dtimeEST = datetime.now(timeEST)
	    curtimeEST = dtimeEST.strftime("%H:%M:%S")

	    timeWET = pytz.timezone("Europe/Madrid")
	    dtimeWET = datetime.now(timeWET)
	    curtimeWET = dtimeWET.strftime("%H:%M:%S")

	    timePA = pytz.timezone("Asia/Manila")
	    dtimePA = datetime.now(timePA)
	    curtimePA = dtimePA.strftime("%H:%M:%S")
    window["-OUTPUT-"].update(curtimeEST)

        #return curtimeEST
        #return curtimeWET
        #return curtimePA
    sleep(1)

while True:
    event, values = window.read()
    print(event, values)
    print()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    else:
        clockfunc()
        sleep(1)
        window.refresh
window.close()