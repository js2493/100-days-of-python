from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
g
# ---------------------------- SEARCH FOR INFO ------------------------------- #
def search():
    file_name = "data.json"
    site = site_input.get().lower()
    try:
        with open(file_name) as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords saved yet!")
    else:
        found_site = False
        for website in data:
            if website.lower() == site:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
                found_site = True
        if not found_site:
            messagebox.showinfo(title="Error", message=f"Password for {site_input.get()} not found!\nPlease try again.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data(file_name, new_data):
    try:
        with open(file_name, "r") as file:
            if os.stat(file_name).st_size == 0:
                data = new_data
            else:
                data = json.load(file)
                data.update(new_data)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


def add_password():
    site = site_input.get()
    user = user_input.get()
    password = password_input.get()
    new_data = {
        site: {
            "username": user,
            "password": password
        }
    }

    if user.replace(" ", "") == "" or password.replace(" ", "") == "" or site.replace(" ", "") == "":
        messagebox.showinfo(title="", message="Please do not leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(
            message=f"Details entered: \nSite: {site}\nUsername: {user}\nPassword: {password}\nIs it OK "
                    f"to save?")
        if is_ok:
            save_data("data.json", new_data)

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
password_button = Button(text="Generate Password", width=13, command=generate_password)
add_button = Button(text="Add", width=36, command=add_password)
search_button = Button(text="Search", width=13, command=search)

site_input = Entry(width=21)
user_input = Entry(width=35)
password_input = Entry(width=21)

site_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
site_input.grid(row=1, column=1)
user_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)
add_button.grid(row=4, column=1, columnspan=2)
password_button.grid(row=3, column=2)
search_button.grid(row=1, column=2)

site_input.focus()
# user_input.insert(0, default_username)

window.mainloop()
