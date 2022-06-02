from secrets import choice
from turtle import Turtle, Screen

frank = Turtle()
colors = ["dark green", "medium blue", "red", "orchid", "sandy brown", "cadet blue", "gold", "light sky blue", "tomato", "rosy brown", "blue violet"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for x in range(num_sides):
        frank.forward(100)
        frank.right(angle)

for sides in range(3, 11):
    frank.pencolor(choice(colors))
    draw_shape(sides)
    

screen = Screen()
screen.exitonclick()