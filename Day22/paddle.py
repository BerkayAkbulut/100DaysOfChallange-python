from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(position)

    def go_up(self):
        self.goto(350, self.ycor() + 20)

    def go_down(self):
        self.goto(350, self.ycor() - 20)
