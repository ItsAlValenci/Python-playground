from turtle import Turtle
import random

class Apple(Turtle): 
    
    #initializing the apple
    def __init__(self):

        #Inheriting from Turtle class + Unique features
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        #move the apple to a new random location
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,269)
        self.goto(x=random_x, y=random_y)

