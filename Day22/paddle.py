from turtle import Turtle

STARTING_POSİTİONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
UP = 20
DOWN = 20
MOVE_DISTANCE=20


class Paddle():
    def __init__(self):
        self.paddle = []
        self.creat_padlle()
        self.head_of_paddle = self.paddle[0]

    def creat_padlle(self):
        for position in STARTING_POSİTİONS:
            self.add_cell(position)

    def add_cell(self, position):
        paddle_object = Turtle(shape=("square"))
        paddle_object.speed(1)
        paddle_object.penup()
        paddle_object.color("white")
        paddle_object.goto(position)
        self.paddle.append(paddle_object)

    def move(self):
        for paddle_num in range(len(self.paddle) - 1, 0, -1):
            new_x = self.paddle[paddle_num - 1].xcor()
            new_y = self.paddle[paddle_num - 1].ycor()
            self.paddle[paddle_num].goto(x=new_x, y=new_y)
        self.head_of_paddle.setheading(90)
        self.head_of_paddle.forward(MOVE_DISTANCE)


    def up(self):
        self.head_of_paddle.setheading(90)
        self.head_of_paddle.forward(UP)
        self.move()
    def down(self):
        self.head_of_paddle.backward(DOWN)
        self.head_of_paddle.setheading(90)
        self.move()