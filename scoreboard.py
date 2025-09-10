from turtle import Turtle

XCOR = 0
YCOR = 270
FONT_SIZE = 12

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(XCOR, YCOR)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", FONT_SIZE, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
       
    