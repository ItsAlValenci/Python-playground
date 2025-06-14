from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPAWN_X = 300


class CarManager:
    def __init__(self):
        super().__init__()
        self.active_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.setheading(180)
        new_car.speed("fastest")
        new_car.penup()
        new_car.shapesize(stretch_len=2,stretch_wid=1)
        new_car.goto(x= CAR_SPAWN_X, y= random.choice(range(-240,260,20)))
        self.active_cars.append(new_car)

    def move(self):
        for car in self.active_cars:
            car.forward(self.move_speed)
        self.active_cars = [car for car in self.active_cars if car.xcor() > -320]

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT




