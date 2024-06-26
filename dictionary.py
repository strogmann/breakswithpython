import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
from os import name, system
import keyboard
import inquirer


def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    #will work for linux, bsd, and mac

print("Python Dictionary by Nicolas Martin")

# Maybe will add translation capability later on...
task = [
    inquirer.List('task',
                  message="Please choose from the the provided list",
                  choices=['Definition', 'Synonym', 'Antonym'],
                  ),
]

clr()  # Clear screen before each new interaction

# Access the user's selected task using dictionary key
answers = inquirer.prompt(task)
user_choice = answers['task']

operation = ""
if user_choice == 'Definition':
    operation = "definition"
elif user_choice == 'Synonym':
    operation = "synonym"
elif user_choice == 'Antonym':
    operation = "antonym"

userword = input("What word do you want to find the " + operation + " of?: ")

#def synonyms(userword):
    #response = requests.get('http://www.thesaurus.com/browse/{}'.format(userword))
   # soup = BeautifulSoup(response.text, 'xml')
   # section = soup.find('section', {'class': 'synonyms-container'})
   # return [span.text for span in soup.findAll('span')]

def synonyms(userword):
    response = requests.get('http://www.thesaurus.com/browse/{}'.format(userword))
    soup = BeautifulSoup(response.text, 'html.parser')
    synonyms_list = soup.find('ul', class_=lambda class_: class_ and 'list' in class_)  # Find first unordered list
    if synonyms_list:
        return [li.text.strip() for li in synonyms_list.find_all('li')]  # Extract text from list items
    else:
        return []  # Return empty list if no synonyms found


if operation == "definition":
    output = PyDictionary.meaning(userword)
elif operation == "synonym":
    output = synonyms(userword)
elif operation == "antonym":
    output = PyDictionary.antonym(userword)
  # Use PyDictionary method
print(output)
