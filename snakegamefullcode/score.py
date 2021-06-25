from turtle import Turtle
ALIGN="center"
FONT =("Courier",24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,310)
        self.score=0
        self.update_score()



    def update_score(self):
        self.write(f"score is {self.score}", align=ALIGN, font=FONT)




    def scoretrack(self):
        self.score+=1
        self.clear()
        self.update_score()






