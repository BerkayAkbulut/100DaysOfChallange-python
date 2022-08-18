from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.y_position = 0
        self.cars = list()
        self.add_car()
        self.levelspeed=0


    def add_car(self):
        car_object = Turtle(shape=("square"))
        car_object.setheading(180)
        car_object.color(random.choice(COLORS))
        car_object.penup()
        self.sayiler = range(-250, 250, 30)
        car_object.shapesize(stretch_wid=1, stretch_len=2)
        self.y_position = random.choice(self.sayiler)
        car_object.goto(250, self.y_position)
        self.cars.append(car_object)
        print(self.cars)

    def move(self):
        for i in self.cars:
            i.forward(MOVE_INCREMENT+self.levelspeed)
