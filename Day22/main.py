from turtle import Turtle, Screen
from paddle import Paddle
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

bar=Paddle()

screen.listen()
screen.onkey(bar.up,"Up")
#screen.onkey(bar.down,"Down")

game_is_on=True
while game_is_on:
    screen.update()
    screen.onkey(bar.up, "Up")
    time.sleep(0.1)








screen.exitonclick()