from turtle import Turtle
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.redraw()

    def update(self, side):
        if side == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.redraw()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def redraw(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=FONT)