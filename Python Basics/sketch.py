from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(15)

def move_backward():
    tim.backward(15)

def turn_right():
    tim.left(15)

def turn_left():
    tim.right(15)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key= "w", fun=move_forward)
screen.onkey(key= "s", fun=move_backward)
screen.onkey(key= "a", fun=turn_left)
screen.onkey(key= "d", fun=turn_right)
screen.onkey(key= "c", fun=clear_screen)

screen.exitonclick()
