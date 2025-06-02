from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT= "Left"
POSITION_Y = 260
POSITION_X = -280

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(POSITION_X, POSITION_Y)
        self.current_level = 0
        self.board_update()

    def board_update(self):
        self.clear()
        self.write(f"LEVEL: {self.current_level}",align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.current_level += 1
        self.board_update()


class Game_Over(Turtle):
        def __init__(self):
            super().__init__()
            self.color("Black")
            self.hideturtle()
            self.penup
            self.goto(0,0)
            self.write("Game Over", align="Center", font=FONT)



    

    
