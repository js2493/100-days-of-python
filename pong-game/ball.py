from turtle import Turtle
import random
SPEED = 0.08


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.up()
        self.speed(10)
        self.x_dir = 0
        self.y_dir = 0
        self.movement_speed = SPEED

    def start(self):
        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])

    def reset(self):
        self.goto(0, 0)
        self.x_dir = 0
        self.y_dir = 0
        self.movement_speed = SPEED

    def move(self):
        new_x = self.xcor() + 10 * self.x_dir
        new_y = self.ycor() + 10 * self.y_dir
        self.goto(new_x, new_y)

    def bounce(self, obstacle):
        if obstacle == "wall":
            self.y_dir *= -1
        else:
            self.x_dir *= -1
