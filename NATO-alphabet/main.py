import pandas
import datetime

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

with open("log.txt", "a") as myfile:
    myfile.write(str(datetime.datetime.now().time()))
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")
    try:
        result = [alphabet_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Not a valid word: Please only use letters")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
