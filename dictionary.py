#Derrick Sung
#This program is used as an Interactive Dictionary that is user-friendly. It is programmed to encounter any errors a User may make.
#These errors can contain misspelling or even capitalization.

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #this is used for any capitalization errors, the program will automatically convert the strings in order to find the correct word.
        return data[word.title()]
    elif word.upper() in data: #this is used for acronym such as "USA" or "NATO"
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word you have entered does not exist. Please make sure it is an existing word."
        else:
            return "I'm sorry, we did not understand the word you have entered."
    else:
        return "The word you have entered does not exist. Please make sure it is an existing word."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
