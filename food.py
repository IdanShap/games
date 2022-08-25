import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        rand_pos_x = random.randint(-280, 280)
        rand_pos_y = random.randint(-280, 270)
        self.goto(x=rand_pos_x, y=rand_pos_y)