from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PLAYER_A_LOCATION = (-350, 0)
PLAYER_B_LOCATION = (350, 0)
TOP_SCORE = 5


#screen setup
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Mini Pong Game")
screen.tracer(0)

game_on = False

# paddle
paddle_a  = Paddle(PLAYER_A_LOCATION)
paddle_b =  Paddle(PLAYER_B_LOCATION)
scoreboard = Scoreboard()
ball = Ball()
screen.update()

screen.listen()
screen.onkey(paddle_a.move_up, "w")
screen.onkey(paddle_a.move_down, "s")
screen.onkey(paddle_b.move_up, "Up")
screen.onkey(paddle_b.move_down, "Down")


game_on = True
while game_on:
    time.sleep(ball.move_speed) #ball speed
    screen.update()
    ball.move()

    # Check for wall collision
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bouce()

    # Check for paddle collision
    if (ball.xcor() > 330 and ball.distance(paddle_b) < 50) or (ball.xcor() < -330 and ball.distance(paddle_a) < 50): #distance measures the distance between the ball center and and paddle dencer
        ball.blocked()


    # Checking collisions with goal Left
    if ball.xcor() < -380:
        scoreboard.a_point()
        ball.goal()
        time.sleep(1)

    # Checking collisions with goal Right 
    if ball.xcor() > 380:
        scoreboard.b_point()
        ball.goal()
        time.sleep(1)
    # Check score conditions
    if scoreboard.score_a >= TOP_SCORE  or scoreboard.score_b >= TOP_SCORE:
        game_on = False

scoreboard.game_over()



















screen.exitonclick()