from turtle import Turtle
ALIGMENT = "center"
FONT = ('Arial', 18)


     

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.get_ranking()
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
            self.update_ranking()
        self.score = 0
        self.score_update()

    def score_increase(self):
        self.score += 1
        self.score_update()

    def get_ranking(self):
        #loading Highest Score
        with open("score_data.txt", mode= "r") as ranking:
            self.highscore = (int(ranking.read()))


    def update_ranking(self):
        #loading Highest Score
        with open("score_data.txt", mode= "w") as ranking:
            ranking.write(f"{self.highscore}")
            


    # def gameover(self):
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)