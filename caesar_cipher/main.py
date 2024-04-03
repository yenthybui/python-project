import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount, cipher_direction):
    end_text = ''
    for i in start_text:
        if i.isdigit() or i.isspace() or not i.isalnum():
            end_letter = i
        else: 
            start_text_index = alphabet.index(i)
            if cipher_direction == 'encode':
                end_letter = alphabet[start_text_index+shift_amount]
            else:
                end_letter = alphabet[start_text_index-shift_amount]
        end_text += end_letter 
    print(f'The {cipher_direction}d text is {end_text}')

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text,shift,direction)

    restart = input('Do you want to restart? y for Yes and others for No: \n')
    if restart != 'y':
        exit()