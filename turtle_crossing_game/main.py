import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()    
    car_manager.create_car()
    car_manager.move_car()
    
    # detect collision with cars
    for car in car_manager.car_list:    
        if car.distance(player) < 20:
            # player.reset_position() #enable this line and disable the two below lines to keep the game auto reset when you lose.
            scoreboard.game_over()
            game_is_on = False
            
    # detect end of level
    if player.ycor() == 270:
        scoreboard.level_up()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()