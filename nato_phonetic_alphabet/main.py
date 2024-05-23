import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')

nato = {row.letter:row.code for (index,row) in df.iterrows()}

def generate_phonetic():
    word = input('Please input a word you want to convert to phonetic code: ').upper()
    
    try:
        code = [nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code)

generate_phonetic()