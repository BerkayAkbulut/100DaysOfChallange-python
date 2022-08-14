from turtle import Turtle

STARTING_POSİTİONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    def __init__(self):
        self.snake = []
        self.creat_snake()
        self.head_of_snake=self.snake[0]

    def creat_snake(self):
        for position in STARTING_POSİTİONS:
            self.add_cell(position)

    def add_cell(self,position):
        snake_object = Turtle(shape=("square"))
        snake_object.speed(10)
        snake_object.penup()
        snake_object.color("white")
        snake_object.goto(position)
        self.snake.append(snake_object)


    def extend(self):
        self.add_cell(self.snake[-1].position())


    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(x=new_x, y=new_y)
        self.head_of_snake.forward(MOVE_DISTANCE)
        #self.snake[0].left(90)

    def up(self):
        if self.head_of_snake.heading()!= DOWN:
            self.head_of_snake.setheading(UP)
    def down(self):
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)
    def left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)
    def right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)
