import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')

nato = {row.letter:row.code for (index,row) in df.iterrows()}

word = input('Please input a word you want to convert to phonetic code: ').upper()

code = [nato[letter] for letter in word]
print(code)