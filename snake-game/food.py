from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        rand_x = random.randint(-14, 14)
        if -3 <= rand_x <= 3:
            rand_y = random.randint(-14, 13)
        else:
            rand_y = random.randint(-14, 14)
        self.goto(rand_x*20, rand_y*20)

    def refresh(self, width, height):
        x_len = int((width/2 - (width/2) % 20)/20)
        y_len = int((height/2 - (height/2) % 20)/20)

        rand_x = random.randint(-(x_len-2), x_len-2)
        if -3 <= rand_x <= 3:
            rand_y = random.randint(-(y_len-2), y_len-3)
        else:
            rand_y = random.randint(-(y_len - 2), y_len - 2)

        self.goto(rand_x*20, rand_y*20)
