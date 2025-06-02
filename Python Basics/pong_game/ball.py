from turtle import Turtle

class Ball(Turtle):
    move_speed = 0.1  # Speed of the ball movement

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self, ):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bouce(self):
        self.y_move *= -1


    def blocked(self):
        self.x_move *= -1
        self.move_speed = max(0.05, self.move_speed - 0.02)  # Increase speed, but not below 0.05

    def goal(self):
        self.move_speed = 0.1  # Reset speed to initial value
        self.goto(0,0)
        self.blocked()

        print("Goal!!")



