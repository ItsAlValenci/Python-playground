import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard,Game_Over

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1,6) ==1:
        carmanager.create_car()
    carmanager.move()

    # checking for car crash
    for car in carmanager.active_cars:
        if player.distance(car)< 20:
            game_over = Game_Over()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.level_up()
        player.restart()
        carmanager.speed_up()





screen.exitonclick()
