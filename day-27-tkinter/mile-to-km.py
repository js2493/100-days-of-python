from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

num_input = Entry()
num_input.grid(row=0, column=1)

text1 = Label(text="Miles", font=("Arial", 16))
text1.grid(row=0, column=2)

text2 = Label(text="is equal to", font=("Arial", 16))
text2.grid(row=1, column=0)

text3 = Label(text="0", font=("Arial", 16))
text3.grid(row=1, column=1)

text4 = Label(text="KM", font=("Arial", 16))
text4.grid(row=1, column=2)


def button_clicked():
    value = int(num_input.get())
    value = value * 1.60934
    text3["text"] = value


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(row=2, column=1)

window.mainloop()