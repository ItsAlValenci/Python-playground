from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIRECTION = 90


class Player(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(DIRECTION)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

