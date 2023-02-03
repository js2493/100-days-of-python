from turtle import Turtle


class Player(Turtle):

    def __init__(self, screen_dimensions):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.seth(90)
        self.up()
        self.speed(0)
        self.max_height = screen_dimensions[1]
        self.reset_self()

    def reset_self(self):
        self.goto(0, -(self.max_height/2-20))

    def move_up(self):
        self.forward(10)

    def move_down(self):
        if self.ycor() > -(self.max_height/2-20):
            self.backward(10)






