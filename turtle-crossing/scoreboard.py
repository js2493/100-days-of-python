from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, screen_dimensions):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.up()
        self.goto(-(screen_dimensions[0]/2-60), screen_dimensions[1]/2-40)
        self.update()

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)

