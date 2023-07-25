from os import name, system
import inquirer
from time import sleep


def clr():
    # windows bleh
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# will work for linux, bsd, and mac

clr()

task = [
    inquirer.List('task',
                  message="What task do you need done?",
                  choices=['Convert to Factored Form', 'Convert to Standard Form', 'Simplify'],
                  ),
]

have = [
    inquirer.List('have',
                  message="What kind of equation are you inputting?",
                  choices=['Factored Form', 'Standard Form'], ),
]

operation = inquirer.prompt(task)
bingus = inquirer.prompt(have)  # what the fuck


def parse_value(value: str) -> dict:
    value_dict = {}

    if value[0] == "-":
        value_dict["sign"] = "-"
        value = value[1:]
    else:
        value_dict["sign"] = "+"

    value_dict["variable"] = find_out_the_variable(value)

    if value_dict["variable"] != "":
        value_split_by_variable = value.split(value_dict["variable"])
        if value_split_by_variable[0] == "":
            value_dict["numeric_part"] = 1
        else:
            value_dict["numeric_part"] = int(value_split_by_variable[0])

        if len(value_split_by_variable) > 1:
            if value_split_by_variable[1] != "":
                power_split = value_split_by_variable[1].split("^")
                value_dict["variable_power"] = int(power_split[1])
    else:
        value_dict["numeric_part"] = int(value)

    return value_dict


def find_out_the_variable(part):
    variable = ""

    for char in part:
        try:
            int(char)
        except ValueError:
            variable = char
            break

    return variable


def split_parenthesized_piece(piece: str) -> list:
    operators = []
    piece_split = []
    for character in piece:
        if character == "+" or character == "-":
            operators.append(character)

    if len(operators) == 1:
        piece_split = piece.split(operators[0])
        if operators[0] == "-":
            piece_split[1] = "-" + piece_split[1]
    if len(operators) == 2:
        piece_split = piece[1:].split(operators[1])
        piece_split[0] = "-" + piece_split[0]
        if operators[1] == "-":
            piece_split[1] = "-" + piece_split[1]

    return piece_split


def factoredtostandard():
    userpieces = input("How many parenthesized pieces are in your equation?: ")
    try:
        pieces = int(userpieces)
    except ValueError:
        print("Invalid value")
        sleep(0.5)
        factoredtostandard()
    if pieces == 2:
        part1 = input("What are the contents of the first parenthesized portion?: ")
        if (")" in part1) or ("(" in part1):
            print("Please exclude parentheses")
            sleep(0.5)
            factoredtostandard()

        part1_split = split_parenthesized_piece(part1)
        part1_values = [parse_value(part1_split[0]), parse_value(part1_split[1])]

        part2 = input("What are the contents of the second parenthesized portion?: ")
        if (")" in part2) or ("(" in part2):
            print("Please exclude parentheses")
            sleep(0.5)
            factoredtostandard()

        part2_split = split_parenthesized_piece(part2)
        part2_values = [parse_value(part2_split[0]), parse_value(part2_split[1])]

        print(part1_values)
        print(part2_values)

        try:
            numerical = int(part1_split[1]) * int(part2_split[1])
            numericalstr = str(numerical)
            if (part1_split[0] == 'x') and (part2_split[0] == 'x'):
                variablemanip = 'x^2'

            midnum = int(part1_split[1]) + int(part2_split[1])
            midnumstr = str(midnum)

            if midnum >= 0:
                sign_mid = "+"
            else:
                sign_mid = ""

            if numerical >= 0:
                sign_numerical = "+"
            else:
                sign_numerical = ""

            
            print(variablemanip + sign_mid + midnumstr + "x" + sign_numerical + numericalstr)
        except ValueError:
            print("Invalid value")
            sleep(0.5)
            factoredtostandard()

    else:
        print(
            "This amount is currently too great for this program. Hopefully this program will be updated in the "
            "future to support this kind of equation.")
        sleep(6)
        clr()
        exit()


if operation["task"] == "Convert to Factored Form" and bingus["have"] == "Factored Form":
    print("Configured to factored form")
    sleep(0.5)
    print("There is nothing to do, closing program.")
    sleep(1)
    exit()
elif operation["task"] == 'Convert to Standard Form' and bingus["have"] == "Factored Form":
    print("Configured to standard form")
    sleep(0.5)
    factoredtostandard()
elif operation["task"] == 'Simplify':
    print("Configured for simplification")