import tkinter

window = tkinter.Tk()
window.title("My First GUI PrograM")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = tkinter.Label(text="Label", font=("Arial", 24))
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# button

def button_clicked():
    print("Clicked")
    text = text_input.get()
    my_label["text"] = text


button1 = tkinter.Button(text="Button 1", command=button_clicked)
button1.grid(row=1, column=1)

button2 = tkinter.Button(text="Button 2", command=button_clicked)
button2.grid(row=0, column=2)
# entry

text_input = tkinter.Entry()
text_input.grid(row=2, column=3)

window.mainloop()
