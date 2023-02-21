import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    french_data = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    original_french_data = pandas.read_csv("data/french_words.csv")
    print(original_french_data)
    french_to_learn = original_french_data.to_dict(orient="records")
else:
    french_to_learn = french_data.to_dict(orient="records")


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=card_front)
    if french_to_learn:
        current_card = random.choice(french_to_learn)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=card_front)
        flip_timer = window.after(3000, func=flip_card)
    else:
        canvas.itemconfig(title, text="", fill="black")
        canvas.itemconfig(word, text="You've Finished!", fill="black")


def remove_word():
    french_to_learn.remove(current_card)
    data = pandas.DataFrame(french_to_learn)
    data.to_csv("data/french_words_to_learn.csv", index=False)
    change_word()


def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_background, image=card_back)


window = tkinter.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_back = tkinter.PhotoImage(file="images/card_back.png")
card_front = tkinter.PhotoImage(file="images/card_front.png")

canvas = tkinter.Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 56, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

right_button = tkinter.Button(image=right_img, highlightthickness=0, command=remove_word)
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=change_word)

right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

change_word()

window.mainloop()
