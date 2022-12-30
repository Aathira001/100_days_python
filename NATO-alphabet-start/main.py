import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_word = input("Enter a Word: ").upper()
codes_for_user = [nato_dictionary[letter] for letter in user_word]
print(f"Here are the codes for your name: \t {codes_for_user}")
