from random import randint, choice
import turtle as t
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

directions = [0,90,180,270]
jill = t.Turtle()

jill.pensize(15)
jill.speed(10)

for sides in range(200):
    jill.pencolor(random_color())
    jill.setheading(choice(directions))
    jill.forward(20)


screen = t.Screen()
screen.exitonclick()