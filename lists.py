from time import sleep
from os import system, name

numbers = [1, 2, 4, 7, 62]

def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

for x in numbers:
    print(x)
    sleep(3)

clr()

print(numbers[2])
sleep(3)

userin = input("Please input a number and I will check to see if it is in the list: ")

try:
    value = int(userin)
except ValueError:
    print("I said a number stupid")
    sleep(0.5)
    exit()

if value in numbers:
	print("This number is in the list!")
else:
	print("This number is not in the list.")