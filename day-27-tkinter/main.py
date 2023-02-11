import tkinter

window = tkinter.Tk()
window.title("My First GUI PrograM")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="Label", font=("Arial",24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button

def button_clicked():
    print("Clicked")
    text = text_input.get()
    my_label["text"] = text


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#entry

text_input = tkinter.Entry()
text_input.pack()




window.mainloop()