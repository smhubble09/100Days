from turtle import Turtle, Screen

bob = Turtle()

for _ in range(15):
    bob.pendown()
    bob.forward(10)
    bob.penup()
    bob.forward(10)

screen = Screen()
screen.exitonclick()