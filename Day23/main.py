import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SECONDS = (3, 4)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard(screen)
cars = CarManager()

screen.listen()
screen.onkeypress(turtle.up, "Up")

index = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    index += 1
    screen.update()
    tic_toc = random.choice(SECONDS)
    if index % tic_toc == 1:
        cars.add_car()
    cars.move()

    if turtle.ycor() > 265:
        scoreboard.reflesh_score()
        cars.levelspeed=scoreboard.score
        turtle.refleh()

    for a_car in cars.cars:
        if a_car.xcor()<-350:
            cars.cars.remove(a_car)
        if turtle.distance(a_car)<25:
            game_is_on=False
            #score.game_over()
