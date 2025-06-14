from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.body.append(new_block)

    def extend(self):
        # Add a block to the end of the body
        self.add_block(self.body[-1].position())

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for part in self.body:
            part.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
        
