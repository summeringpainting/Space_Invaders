from turtle import Turtle


class Ship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.tilt(-30)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
