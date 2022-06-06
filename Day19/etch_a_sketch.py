from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forwards,key="w")
screen.onkey(fun=move_backwards,key="s")
screen.onkey(fun=rotate_left,key="a")
screen.onkey(fun=rotate_right,key="d")
screen.onkey(fun=clear_screen,key="c")
screen.exitonclick()