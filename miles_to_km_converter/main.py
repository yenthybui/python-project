import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=250, height=150)
window.config(padx=20, pady=20) #add padding/margin

#Label
label_miles = tkinter.Label(text='Miles')
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text='is equal to')
label_equal.grid(column=0, row=1)

label_calculation = tkinter.Label(text='0')
label_calculation.grid(column=1, row=1)

label_km = tkinter.Label(text='Km')
label_km.grid(column=2, row=1)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=1,row=0)

#Button
def button_clicked():
    input_miles = float(input.get())
    output_km = round(input_miles*1.60934, 2)
    label_calculation.config(text=output_km)

button = tkinter.Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()