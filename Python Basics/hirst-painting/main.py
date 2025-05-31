import colorgram

# Extract 6 colors from an image.
RGB_only = []
colors = colorgram.extract('image.png', 10)

for element in colors:
    r = element.rgb.r
    g = element.rgb.g
    b = element.rgb.b
    rgb_code = (r, g, b)
    RGB_only.append(rgb_code)

# color_list = [(249, 249, 248), (248, 246, 247), (190, 171, 114), (227, 231, 235), (158, 174, 191), (240, 245, 243)]
color_list = RGB_only

import turtle as t
import random as rand  


## Extra random RGB ##
import turtle as t
import random as rand

def random_paint(Column,Row):
    #locations
    X = -250
    Y = -280
    
    
    turty = t.Turtle()
    turty.penup()
    turty.goto(X, Y)
    turty.shape("turtle")
    t.colormode(255)
    turty.speed("fastest")
    

    for row in range (Row):
        Y += 50
        turty.goto(X, Y)
        for i in range (Column):
            turty.dot(20,rand.choice(color_list))
            turty.forward(50)


random_paint(10,10)






screen = t.Screen()
screen.exitonclick()

