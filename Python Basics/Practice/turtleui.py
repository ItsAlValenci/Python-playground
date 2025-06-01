import turtle
from turtle import Turtle,Screen

# ## Challenge 1: making a square
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("dark green")

# def draw_square():
#     for i in range (4):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(90)
# draw_square()

## Challenge 2: Dashed line
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("dark green")

# def dahsed_line():
#     for i in range (20):
#         timmy_the_turtle.forward(3)
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(3)
#         timmy_the_turtle.pendown()
# dahsed_line()

# ## Challenge 3: Draw shapes
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("dark green")

# def draw_shape(start_shape):
#         angle = 360/start_shape
#         for i in range(start_shape):
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(angle)

# for shape_n in range(3,11):
#       draw_shape(shape_n)

# ## challenge 4: Random Walk
# import random as rand
# colors_list = ["IndianRed1", "cornflower blue", "aquamarine2", "orange", "plum2", "dark gray", "LightPink"]
# sides = [0, 90, 180, 270 ]
# line_size = [3,4,5,6,7,8,9]

# def random_walk():
#     turty = Turtle()
#     turty.shape("turtle")
#     turty.speed(8)

#     for i in range (150):
#         turty.color(rand.choice(colors_list))
#         turty.pensize(rand.choice(line_size))
#         turty.right(rand.choice(sides))
#         turty.forward(40)

# random_walk()

# ## Extra random RGB ##
# import turtle as t
# import random as rand


# def random_color():
#     r = rand.randint(0,255)
#     g = rand.randint(0,255)
#     b = rand.randint(0,255)

#     random_color = (r,g,b)
#     return random_color

# def random_walk2():
#     turty = t.Turtle()
#     turty.shape("turtle")
#     t.colormode(255)
#     turty.speed("fastest")

#     sides = [0, 90, 180, 270 ]
#     line_size = [3,4,5,6,7,8,9]

#     for i in range (150):
#         turty.color(random_color())
#         turty.pensize(rand.choice(line_size))
#         turty.right(rand.choice(sides))
#         turty.forward(40)

# random_walk2()

# screen = t.Screen()
# screen.exitonclick()

## Challenge 5: Draw a spirograph
import random as rand    

def draw_spirograph(times: int):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.speed("fastest")
    timmy.color("dark green")
    turtle.colormode(255)

    def colors_rand():
        r = rand.randint(0, 255)
        g = rand.randint(0, 255)
        b = rand.randint(0, 255)

        colors_rand = (r, g, b)
        return (r, g, b)
    
    for i in range ( int(360/times)):
        timmy.color(colors_rand())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + times)
    

draw_spirograph(10)





screen = Screen()
screen.exitonclick()

