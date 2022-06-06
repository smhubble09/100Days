from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "brown", "green", "blue", "purple"]
all_turtles = []

y_coord = -66
for item in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_coord)
    all_turtles.append(new_turtle)
    y_coord += 33

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!") 
        turtle.forward(randint(0,10))
    

screen.exitonclick()