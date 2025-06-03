from turtle import Turtle
ALIGMENT = "center"
FONT = ('Arial', 18)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.score_update()
        
    def score_update(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.highscore}", align= ALIGMENT, font= FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.score_update()

    def score_increase(self):
        self.score += 1
        self.score_update()

    # def gameover(self):
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)