import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("My Turtle Game")
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.onkeypress(player.up,"Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Generate new car
    car_manager.create_car()
    #Move cars
    car_manager.move_cars()

    #Detect when player reached top and increase level
    if player.is_at_finish_line():
        player.refresh()
        scoreboard.update_level()
        car_manager.level_up()
    
    #Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()