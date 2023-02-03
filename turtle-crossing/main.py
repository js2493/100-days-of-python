import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
dim = (WINDOW_WIDTH, WINDOW_HEIGHT)

game_level = 1


screen = Screen()
screen.tracer(0)

scoreboard = Scoreboard(dim)
player = Player(dim)
car_manager = CarManager(dim)

screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_on = True
car_manager.generate_cars()

print(f"Level: {game_level}, #Cars: {len(car_manager.car_list)}, Speed: {car_manager.speed}")

while game_on:
    time.sleep(0.01)
    screen.update()
    car_manager.move_cars(game_level)

    # next level
    if player.ycor() >= WINDOW_HEIGHT/2-20:
        game_level += 1
        player.reset_self()
        scoreboard.update()
        car_manager.next_level(game_level)
        print(f"Level: {game_level}, Cars: {len(car_manager.car_list)}, Speed: {car_manager.speed}")

    # game over
    for car in car_manager.car_list:
        if abs(car.ycor() - player.ycor()) < 20 and abs(car.xcor() - player.xcor()) < 20:
            print("shit on")
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
