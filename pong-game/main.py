from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(360, 0)
left_paddle = Paddle(-370, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(ball.start, "space")

game_on = True

while game_on:

    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -270:
        ball.bounce("wall")

    if ball.xcor() == 340:
        if right_paddle.touching(ball):
            ball.bounce("paddle")
            ball.movement_speed *= 0.9

    elif ball.xcor() == -350:
        if left_paddle.touching(ball):
            ball.bounce("paddle")
            ball.movement_speed *= 0.9

    if ball.xcor() == -400:
        scoreboard.update("right")
        ball.reset()

    elif ball.xcor() == 400:
        scoreboard.update("left")
        ball.reset()


