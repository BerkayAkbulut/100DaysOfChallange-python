from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.score=0
        # self.clear()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.write(arg=self.score,move=False,align="center",font=FONT)
        self.hideturtle()

    def reflesh_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, move=False, align="center", font=("Arial", 24, "normal"))