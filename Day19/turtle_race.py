from turtle import Turtle, Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple","black"]
all_turtles=[]

distance=[1,3,5,7]
y_positions=[150,100,50,0,-50,-100,-150]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>211:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You are winner!")
            else:
                print(f"You are loser :p",f"The winner is {winning_color}",sep="\n")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()