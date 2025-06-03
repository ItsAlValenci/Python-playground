from turtle import Screen
import time
import random 
from snake import Snake
from food import Apple
from scoreboard import Scoreboard

#screen setup
screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Skeany Snake Game")
screen.tracer(0)


snake = Snake()
apple = Apple()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(apple) < 15:
        apple.refresh()
        snake.extend()
        scoreboard.score_increase()

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -290 or 
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
            scoreboard.reset()
            snake.reset()
            time.sleep(0.5)


    # Detect collision with tail
    for block in snake.body[1:]:  # Skip the head
        if snake.head.distance(block) < 10:
            scoreboard.reset()
            snake.reset()
            time.sleep(0.5)


     




















screen.exitonclick()