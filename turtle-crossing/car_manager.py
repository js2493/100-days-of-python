from car import Car
import random

STARTING_CARS = 12


class CarManager:
    def __init__(self, dim):
        self.car_list = []
        self.speed = 1
        self.dim = dim

    def generate_cars(self):
        for x in range(0, STARTING_CARS):
            car = Car(self.dim)
            car.reset()
            self.car_list.append(car)

    def move_cars(self, level):
        for car in self.car_list:
            if car.xcor() < -300:
                car.reset()
            car.move(level)

    def next_level(self, level):
        for car in self.car_list:
            car.reset()
        if level % 2 == 1:
            new_car = Car(self.dim)
            new_car.reset()
            self.car_list.append(new_car)
        self.speed = (int(level/2) + 10)/10

