from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"{self.l_score}       {self.r_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self, scorer):
        self.clear()
        if scorer == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()

    def check_score(self):
        if self.l_score == 5:
            self.game_over("Left Side")
        elif self.r_score == 5:
            self.game_over("Right Side")
        else:
            return True

    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"{winner} wins!", align=ALIGNMENT, font=FONT)
        return False