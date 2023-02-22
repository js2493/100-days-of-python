THEME_COLOR = "#375362"
import tkinter as tk
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.not_ended = True
        self.not_answered = True
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question, fill=THEME_COLOR)
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.not_answered = True
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.not_ended = False
            self.score.config(text="")
            self.canvas.itemconfig(self.question, text=f"You've finished! Score: {self.quiz.score}")

    def false(self):
        if self.not_answered and self.not_ended:
            self.not_answered = False
            self.give_feedback(self.quiz.check_answer("False"))

    def true(self):
        if self.not_answered and self.not_ended:
            self.not_answered = False
            self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.question, fill="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(500, self.get_next_question)
