import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
#tim.shape("turtle")
tim.width(2)
tim.speed(200)


def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb=(r,g,b)
    return rgb
for x in range(72):
    tim.color(random_color())
    tim.right(5)
    for i in range(90):
        tim.forward(16)
        tim.right(4)

screen = Screen()
screen.exitonclick()