from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 10


class Car(Turtle):
    def __init__(self, screen_dimensions):
        super().__init__()
        self.shapesize(1, 2)
        self.seth(180)
        self.shape("square")
        self.penup()
        self.max_height = screen_dimensions[1]
        self.max_width = screen_dimensions[0]

    def move(self, level):
        speed = (int(level/2) + STARTING_SPEED)/10
        self.forward(speed)

    def reset(self):
        self.color(random.choice(COLORS))
        self.goto(random.randint(self.max_width/2, self.max_width*1.5), random.randint(-(self.max_height/2-50), self.max_height/2-50))
