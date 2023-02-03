from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_loc, y_loc):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.go_to(x_loc, y_loc)

    def go_to(self, x, y):
        self.penup()
        self.speed("fastest")
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 230:
            self.move(1)

    def go_down(self):
        if self.ycor() > -230:
            self.move(-1)

    def move(self, direction):
        new_y = self.ycor() + 20*direction
        self.goto(self.xcor(), new_y)

    def touching(self, ball):
        distance = abs(self.ycor()-ball.ycor())
        if distance <= 60:
            return True
        else:
            return False
