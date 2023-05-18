from time import sleep
from os import system, name

def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

clr()

userin = input("Please enter a number: ")

try:
    value = int(userin)
except ValueError:
    print("I said a number stupid")
    sleep(0.5)
    exit()
if value < 0:
    print("Why did you pick a negative number goofy")
    sleep(0.5)
else:
    print("Alright, thanks for picking a normal number")
    sleep(0.5)