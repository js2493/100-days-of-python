from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:", width=13)
user_label = Label(text="Username:", width=13)
password_label = Label(text="Password:", width=13)
password_button = Button(text="Generate Password", width=13)
add_button = Button(text="Add", width=36)
site_input = Entry(width=35)
user_input = Entry(width=35)
password_input = Entry(width=21)

site_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
site_input.grid(row=1, column=1, columnspan=2)
user_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
add_button.grid(row=4, column=1, columnspan=2)
password_button.grid(row=3, column=2)

window.mainloop()
