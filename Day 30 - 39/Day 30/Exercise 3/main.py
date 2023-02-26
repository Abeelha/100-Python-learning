# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
incorrect_input = True

data = pandas.read_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 30 - 39/Day 30/Exercise 3/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while incorrect_input:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        incorrect_input = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        word = input("Enter a word: ").upper()
