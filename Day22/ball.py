from random import choice
from turtle import Turtle

MOVE_SPEED = 20
STARTING_ANGLES = [45, 135, 225, 315]
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(0)
        self.refresh()

    def change_heading(self, collision_source):
        if collision_source == "wall":
            self.setheading(360 - self.heading())
        else:
            self.setheading(180 - self.heading())

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.change_heading("wall")
        self.forward(MOVE_SPEED)

    def refresh(self):
        self.move_speed = .1
        self.goto(0,0)
        self.setheading(choice(STARTING_ANGLES))

    def increase_speed(self):
        self.move_speed *= .9