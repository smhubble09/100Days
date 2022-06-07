from random import randint
from turtle import Turtle

MOVE_DISTANCE = 20
class Paddle(Turtle):
    def __init__(self, coord) -> None:
        super().__init__()
        self.goto(coord)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid= 0.5)
        self.color("white")
        self.speed(0)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)