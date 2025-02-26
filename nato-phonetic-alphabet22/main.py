import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for _, row in data.iterrows()}


def get_input():
    word = input("Enter a word: ").upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        get_input()
    else:
        return output_list


get_input()
