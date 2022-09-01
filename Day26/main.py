import pandas as pd

alphabet_csv_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in alphabet_csv_df.iterrows()}
print(nato_alphabet)
name = input("Enter a word: ").upper()

spell = [nato_alphabet[letter] for letter in name]
print(spell)