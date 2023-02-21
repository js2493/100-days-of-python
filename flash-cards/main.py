import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashcards")

french_csv = pandas.read_csv("data/french_words.csv")
french_words = [french_csv.French.to_list(), french_csv.English.to_list()]

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = tkinter.PhotoImage(file="images/card_back.png")
card_front = tkinter.PhotoImage(file="images/card_front.png")

canvas = tkinter.Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 56, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

right_button = tkinter.Button(image=right_img, highlightthickness=0)
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0)

right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)


window.mainloop()
