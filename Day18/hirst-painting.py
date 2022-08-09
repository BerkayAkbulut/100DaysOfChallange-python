import colorgram
import turtle
from turtle import Screen
import random

rgb_colors=[]
colors=colorgram.extract("photo.jpg",25)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

color_list=[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

turtle.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

number_of_dots=101
for dot_count in range(1,number_of_dots):
    turtle.dot(20,random.choice(color_list))
    turtle.forward(50)

    if dot_count%10==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()

