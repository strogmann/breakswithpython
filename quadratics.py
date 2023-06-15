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
#print(answer["task"])

#def factor():


if operation["task"] == "Convert to Factored Form" and bingus['have'] == "Factored Form":
    print("Configured to factored form")
elif answer["task"] == 'Convert to Standard Form':
    print("Configured to standard form")
elif answer["task"] == 'Simplify':
    print("Configured for simplification")

