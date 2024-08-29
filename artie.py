#Version 0.1

from os import name, system
import random
import inquirer

affirm = ["good", "Good", "great", "Great", "Yes", "yes"]
deny = ["bad", "Bad", "Not Good", "not good", "No", "no"]
list_check = ["check", "Check", "Debug", "debug"]
known_words = ["dog", "apple", "cat", "I", "am", "is", "eat", "breathe", "pet", "an", "a", "me", "for", "you", "alive"]
subjects = ["dog", "apple", "cat", "me", "you", ]
indefarticles = []
verbs = []
phrases = []
structures = []

def clr():
    # windows bleh
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clr()

task = [
    inquirer.List('task',
                  message="What will you do?",
                  choices=['Allow Artie to learn', 'Make Artie form phrases'],
                  ),
]

operation = inquirer.prompt(task)

def forming():
    print("currently unable to do this task, will add soon.")

def learning():
    string = random.choice(known_words) + " " + random.choice(known_words) + " " + random.choice(known_words)
    print(string)
    guide = input()
    if guide in affirm:
        phrases.append(string)
        new_word = input()
        if new_word not in known_words:
            known_words.append(new_word)
        else:
            learning()
        learning()
    elif guide in deny:
        learning()
    elif guide in list_check:
        print(known_words)
        print(phrases)
        learning()

learning()

if operation == 'Allow Artie to learn':
    learning()
elif operation == 'Make Artie form phrases':
    forming()
