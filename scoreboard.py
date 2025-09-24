from turtle import Turtle

XCOR = 0
YCOR = 270
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score() # Initialize high score from file
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(XCOR, YCOR)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",  align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()
       
    def read_high_score(self):
        try:
            with open("data.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0
            
    def write_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
    