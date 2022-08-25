from turtle import Turtle


class Enemy(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - .08
        new_y = self.ycor() - .02
        self.goto(new_x, new_y - .05)

    def go_right(self):
        new_x = self.xcor() + .08
        new_y = self.ycor() + .02
        self.goto(new_x, new_y - .05)
