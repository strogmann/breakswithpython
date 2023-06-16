from os import name, system
import inquirer
from time import sleep
def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

clr()

task = [
    inquirer.List('task',
    message = "What task do you need done?",
    choices = ['Convert to Factored Form', 'Convert to Standard Form', 'Simplify'],
    ),
]

have = [
    inquirer.List('have',
    message = "What kind of equation are you inputting?",
    choices = ['Factored Form', 'Standard Form'],),
]

operation = inquirer.prompt(task)
bingus = inquirer.prompt(have)

def factoredtostandard():
    userpieces = input("How many parenthesized pieces are in your equation?: ")
    try:
        pieces = int(userpieces)
    except ValueError:
        print("Invalid value")
        sleep(0.5)
        factoredstostandard()
    if pieces == 2:
        print(":)")
    elif pieces == 3:
        print(":(")
    else:
        print("This amount is currently too great for this program. Hopefully this program will be updated in the future to support this kind of equation.")
        sleep(10)
        clr()
        exit()


if operation["task"] == "Convert to Factored Form" and bingus["have"] == "Factored Form":
    print("Configured to factored form")
    sleep(0.5)
    factoredtostandard()

elif operation["task"] == 'Convert to Standard Form':
    print("Configured to standard form")
elif operation["task"] == 'Simplify':
    print("Configured for simplification")
