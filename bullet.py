import time
from ship import Ship

from turtle import Turtle


# ship = Ship((0, -250))
class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = .1
        self._rotate(90)
        self.y_move = .1
        self.move_speed = 0.01
        self.shapesize(.2, .7, .2)
        self.bull = self.clone()
        self.bully = self.bull.clone()
        self.bully.right(180)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def reset_position(self):
        pass

    def shoot(self):
        print("shoot")
        if self.bull.ycor() == -350:
            self.bull.goto(self.xcor(), self.ycor() + 20)
        # self.bull.goto(self.bull.xcor(), self.bull.ycor() + 20)
