import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    user_word = input("Enter a Word: ").upper()
    try:
        codes_for_user = [nato_dictionary[letter] for letter in user_word]
    except KeyError:
        print(f"Sorry, {user_word} contains a character that is not a letter. Please enter a valid name ")
        generate_phonetic()
    else:
        print(f"Here are the codes for your name: \t {codes_for_user}")


generate_phonetic()
