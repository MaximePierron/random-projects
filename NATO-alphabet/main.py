import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

name_to_code = input("Enter your name:\n").upper()
coded_name = [nato_dict[letter] for letter in [*name_to_code]]

print(coded_name)

