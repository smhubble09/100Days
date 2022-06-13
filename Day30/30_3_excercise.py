import pandas

data = pandas.read_csv("Day30/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO: Catch the exception and make sure the code runs without crashing.
invalid_word = True
while invalid_word:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the word please")
    else:
        print(output_list)
        invalid_word = False
