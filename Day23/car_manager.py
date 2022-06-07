from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "brown", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.speed(0)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250,250))
            self.all_cars.append(new_car)    

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
