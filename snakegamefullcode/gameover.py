from turtle import Turtle
from score import *
class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
    def gameoverupdate(self):
        self.write("GAME OVER",align=ALIGN, font=FONT)