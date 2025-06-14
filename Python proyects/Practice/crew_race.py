from turtle import Turtle, Screen
import random as rand

race_on = False

screen = Screen()
screen.setup(width=800, height=600 )
user_bet = screen.textinput(title= "Make your Bets!!", prompt= "Which guy will win the race?? select a Color: " )
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtle(turtle_color: str, color_index= int):

    Y = 130 -(50 * color_index)

    racer = Turtle(shape="turtle")
    racer.color(turtle_color)
    racer.penup()
    racer.goto(x= -380,y=Y)
    racer.speed("fastest")
    all_turtles.append(racer)


for i in colors:
    create_turtle(i, colors.index(i))
    

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            race_on = False
            print(f"\n\nthe winner is the {turtle.pencolor()} turtle")
            if user_bet == turtle.pencolor():
                print("\n\nYou won!!")
            else:
                print("\nYou lost!!")
            
        else:
            random_distance = rand.randint(0,10)
            turtle.forward(random_distance)










screen.exitonclick()
