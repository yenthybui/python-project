from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8,10)
nr_numbers = random.randint(2,4)
nr_symbols = random.randint(2,4)

def generate_password():
    password = []
    
    letter = [random.choice(letters) for i in range(0, nr_letters)]
    symbol = [random.choice(symbols) for i in range(0, nr_symbols)]    
    number = [random.choice(numbers) for i in range(0, nr_numbers)]
    
    password = letter + symbol + number
    
    random.shuffle(password)
    password = ''.join(password)
    
    #delete any pre-existed text and insert generated password
    password_entry.delete(0, 'end')
    password_entry.insert(END, string=password)
    
    #copy the password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website == '' or email == '' or password == '':
        messagebox.showinfo(title='Oops', message='Please complete all fields.')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"Website: {website} \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        
        if is_okay:
            password = f'{website} | {email} | {password}\n'
            with open('data.txt', 'a') as file:
                file.write(password)
            #Clear all entries
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
              
#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Button
password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# ----
window.mainloop()