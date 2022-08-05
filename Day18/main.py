import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
#tim.shape("turtle")


def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb=(r,g,b)
    return rgb



tim.width(4)
tim.speed(10)

turn=[0,90,180,270]
while True:
    tim.color(random_color())
    tim.forward(25)
    tim.right(random.choice(turn))

screen = Screen()
screen.exitonclick()