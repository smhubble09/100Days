from secrets import choice
from turtle import Turtle, Screen

paul = Turtle()
colors = ["dark green", "medium blue", "red", "orchid", "sandy brown", "cadet blue", "gold", "light sky blue", "tomato", "rosy brown", "blue violet"]
directions = [0,90,180,270]
paul.pensize(15)
paul.speed(10)

for sides in range(200):
    paul.pencolor(choice(colors))
    paul.setheading(choice(directions))
    paul.forward(20)


screen = Screen()
screen.exitonclick()