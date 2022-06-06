
import pandas as pd

phone_data = pd.read_csv("nato_phonetic_alphabet.csv")


phone_dict = {row.letter:row.code for (index,row) in phone_data.iterrows()}


def input_nato():
    user_input = input("Input a word: ").upper()
    try:
        phone_code = [phone_dict[letter] for letter in user_input if letter != " "]
    except KeyError:
        print("Sorry Only Letter inputs allowed")
        input_nato()
    else:
        print(phone_code)


input_nato()