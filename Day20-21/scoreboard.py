from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.read_file()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):  
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()

    def read_file(self):
        with open("./Day20-21/data.txt") as file:
                self.high_score = int(file.read())

    def write_file(self):
        with open("./Day20-21/data.txt", mode="w") as file:
                file.write(str(self.score))