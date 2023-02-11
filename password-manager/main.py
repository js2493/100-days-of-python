from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    site = site_input.get()
    user = user_input.get()
    password = password_input.get()

    if user.replace(" ", "") == "" or password.replace(" ", "") == "" or site.replace(" ", "") == "":
        messagebox.showinfo(title="", message="Please do not leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(message=f"Details entered: \nSite: {site}\nUsername: {user}\nPassword: {password}\nIs it OK "
                                               f"to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{site} | {user} | {password}\n")
                site_input.delete(0, END)
                user_input.delete(0, END)
                password_input.delete(0, END)
                # user_input.insert(0, default_username)


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
add_button = Button(text="Add", width=36, command=add_password)
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

site_input.focus()
#user_input.insert(0, default_username)

window.mainloop()
