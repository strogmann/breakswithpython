from time import sleep
from os import system, name

userop = ""

def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

clr()
def operator():
    userop = input("Please input an operator: ")

    if userop == "x" or userop == "*":
        mult()
    elif userop == "/":
        div()
    elif userop == "-":
        sub()
    elif userop == "+":
        add()
    else:
        print("This is not a recognized operator")
        sleep(0.5)
        operator()

def mult():
    multuserval1 = input("Please insert your first factor: ")
    try:
        multval1 = int(multuserval1)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        mult()

    multuserval2 = input("Please insert your second factor: ")
    try:
        multval2 = int(multuserval2)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        mult()
    product = multval1*multval2
    print("The product is: " + str(product))
    sleep(0.5)
    operator()

def div():
    divuserval1 = input("Please insert your numerator: ")
    try:
        divval1 = int(divuserval1)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        div()

    divuserval2 = input("Please insert your denominator: ")
    try:
        divval2 = int(divuserval2)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        div()

    quotient = divval1/divval2
    print("The quotient is: " + str(quotient))
    sleep(0.5)
    operator()

def add():
    adduserval1 = input("Please insert your first addend: ")
    try:
        addval1 = int(adduserval1)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        add()

    adduserval2 = input("Please insert your second addend: ")
    try:
        addval2 = int(adduserval2)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        add()

    sum = addval1+addval2
    print("The sum is: " + str(sum))
    sleep(0.5)
    operator()

def sub():
    subuserval1 = input("Please insert your minuend: ")
    try:
        subval1 = int(subuserval1)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        sub()

    subuserval2 = input("Please insert your subtrahend: ")
    try:
        subval2 = int(subuserval2)
    except ValueError:
        print("You have inserted a non-numerical character")
        sleep(0.5)
        sub()

    difference = subval1-subval2
    print("The difference is: " + str(difference))
    sleep(0.5)
    operator()

operator()



#These if/elif statements can be contained in a function later on to allow the program to rerun it after a
#calculation has been performed instead of having to rerun the whole program
