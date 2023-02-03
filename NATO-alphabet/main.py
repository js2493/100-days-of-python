
import pandas


# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

word = input("Enter a word: ")
result = [alphabet_dict[letter.upper()] for letter in word]
print(result)
