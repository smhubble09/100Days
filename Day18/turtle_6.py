from random import randint, choice
import turtle as t
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

directions = [0,90,180,270]
hoyt = t.Turtle()

hoyt.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        hoyt.pencolor(random_color())
        hoyt.setheading(hoyt.heading() + size_of_gap)
        hoyt.circle(100)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()