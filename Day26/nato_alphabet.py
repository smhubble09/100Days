import pandas
#TODO 1. Create a dictionary in this format: {"A": "Alpha", "B": "Beta"}
data = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

nato_list = [nato_dict[letter] for letter in user_input]
print(nato_list)