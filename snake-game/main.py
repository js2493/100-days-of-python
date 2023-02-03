from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

game_on = True
speed = 0.08
grown = False

while game_on:

    screen.update()

    time.sleep(speed)

    if not snake.has_moved:
        snake.move_forward()

    # grow when touching food
    if snake.head.distance(food) < 15:
        food.refresh(screen.window_width(), screen.window_height())
        snake.grow()
        speed = speed * 0.95
        scoreboard.increase_score()
        grown = True

    max_x = int(screen.window_width() / 2) - 5
    max_y = int(screen.window_height() / 2) - 5

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            print("You ate yourself!")
            print(f"Final Score: {scoreboard.score} points")

    # detect collision with wall
    if snake.head.xcor() > max_x or snake.head.xcor() < -max_x or snake.head.ycor() > max_y or snake.head.ycor() < -max_y:
        # screen.bye()
        print("You lost!")
        print(f"Final Score: {scoreboard.score} points")
        scoreboard.reset()
        snake.reset()

    snake.has_moved = False

screen.exitonclick()
