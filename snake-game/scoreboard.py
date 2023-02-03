from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0, 270)
        self.update()
    # def align(self, height):
    #     self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()


