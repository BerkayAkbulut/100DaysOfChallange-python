from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.score=0
        # self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=self.score,move=False,align="center",font=("Courier",24 , "normal"))
        self.hideturtle()

    def reflesh_score(self):
        self.score+=1
        self.clear()
        self.write(arg=self.score, move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        #self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align="center", font=("Courier", 24, "normal"))
