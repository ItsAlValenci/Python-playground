from turtle import Turtle
ALIGNMENT = "center"
TEXT_FONT = ("Arial", 35, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score_a = 0
        self.score_b = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f" {self.score_a} | {self.score_b} ",align=ALIGNMENT, font=TEXT_FONT)

    def a_point(self):
        self.score_a += 1
        self.score_update()

    def b_point(self):
        self.score_b += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=TEXT_FONT)
        self.goto(0, -40)

        