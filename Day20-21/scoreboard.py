from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.score=0
        self.high_score =0
        with open("data.txt", mode="r") as f:
            self.high_score = f.read()
        #f.close()
        # self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score} | High score: {self.high_score}",move=False,align="center",font=("Courier",24 , "normal"))
        self.hideturtle()

    def reflesh_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score: {self.score} | High score: {self.high_score}",move=False,align="center",font=("Courier",24 , "normal"))

    def game_over(self):
        with open("data.txt", mode="r+") as ff:
            if self.score>int(self.high_score):
                ff.write(str(self.score))
            else:
                ff.write(int(self.high_score))
            #ff.close()

        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(arg=f"Score: {self.score} | High score: {self.high_score}",move=False,align="center",font=("Courier",24 , "normal"))
