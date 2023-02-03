from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.has_moved = False

    def create_snake(self):
        for x in range(3):
            self.segments.append(Turtle())
            self.segments[x].penup()
            self.segments[x].color("white")
            self.segments[x].shape("turtle")
            self.segments[x].goto(20 - 20 * x, 0)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].seth(self.segments[seg_num - 1].heading())
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.turn(LEFT)

    def right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.turn(RIGHT)

    def down(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.turn(DOWN)

    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.turn(UP)

    def turn(self, direction):
        self.move_forward()
        self.has_moved = True
        self.head.seth(direction)

    def grow(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("turtle")
        tail_len = len(self.segments) - 1
        # tail_direction = self.segments[tail_len].heading()
        tail_x = self.segments[tail_len].xcor()
        tail_y = self.segments[tail_len].ycor()
        tail2_x = self.segments[tail_len - 1].xcor()
        tail2_y = self.segments[tail_len - 1].ycor()

        diff_x = tail_x - tail2_x
        diff_y = tail_y - tail2_y

        new_segment.goto(tail_x + diff_x, tail_y + diff_y)
        self.segments.append(new_segment)

    def reset(self):
        for snake in self.segments:
            snake.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
