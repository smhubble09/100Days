from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


game_is_on = True

ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    
    #Detect collision with paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330 or ball.distance(r_paddle) < 50 and ball.xcor() > 330 :
        ball.change_heading("paddle")
        ball.increase_speed()

    #Detect if paddle misses ball
    if ball.xcor() > 400:
        scoreboard.increase_score("left")
        ball.refresh()
    elif ball.xcor() < -400:
        scoreboard.increase_score("right")
        ball.refresh()
    
    game_is_on = scoreboard.check_score()




screen.exitonclick()