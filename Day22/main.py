from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.tracer(1)
ball=Ball()
screen.tracer(0)

game_is_on=True
tic_toc=0.1
while game_is_on:
    time.sleep(tic_toc)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or  ball.distance(l_paddle)<50 and ball.xcor()< - 320:
        ball.bounce_x()
        if tic_toc>0.008:
            tic_toc-=0.00
    if ball.xcor()>400:
        ball.reset_position()
        tic_toc = 0.1

    if ball.xcor() < - 400:
        ball.reset_position()
        tic_toc = 0.1











screen.exitonclick()