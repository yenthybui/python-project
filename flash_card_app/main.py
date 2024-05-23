BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
# --------------------------- WORD GENERATION --------------------------------- #
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
finally:
    word_list = df.to_dict(orient='records')

current_card = {}

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    
    flip_timer = window.after(3000, flip_card)

# --------------------------- CARD FLIPPING ----------------------------------- #
def flip_card():
        canvas.itemconfig(card, image=card_back)
        canvas.itemconfig(title_text, text='English', fill='white')
        canvas.itemconfig(word_text, text=current_card['English'], fill='white')
        
# ------------------------- REMOVE KNOWN WORDS -------------------------------- #
def remove_word():
    word_list.remove(current_card)
    
    #save the unknown words to a file to reuse for next time
    unknown_word_list = pd.DataFrame(word_list)
    unknown_word_list.to_csv('data/words_to_learn.csv', index=False)
    
    generate_word()

# ------------------------------ UI SETUP ------------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card = canvas.create_image(410, 270, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

#Button
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=remove_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=generate_word)
wrong_button.grid(column=0, row=1)



# ------
generate_word()

window.mainloop()

