from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-270, 270), y=randint(-270, 270))




