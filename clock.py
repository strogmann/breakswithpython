from datetime import datetime
from os import system, name
from time import sleep
import pytz

#zones = pytz.all_timezones
#print(zones)

def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

while True:
	clr()
	timeEST = pytz.timezone("America/New_York")
	dtimeEST = datetime.now(timeEST)
	curtimeEST = dtimeEST.strftime("%H:%M:%S")

	timeWET = pytz.timezone("Europe/Madrid")
	dtimeWET = datetime.now(timeWET)
	curtimeWET = dtimeWET.strftime("%H:%M:%S")

	timePA = pytz.timezone("Asia/Manila")
	dtimePA = datetime.now(timePA)
	curtimePA = dtimePA.strftime("%H:%M:%S")
	
	print("TUI Clock")
	print("New York, USA: " + curtimeEST)
	print("Madrid, ES: " + curtimeWET)
	print("Manila, PHIL: " + curtimePA)
	
	sleep(1)

#This terminal-based international clock was made by Nicolas Martin