# Theodoro Bertol Dev (Abeelha) #
# || Day 21 of #100DaysOfCode || #

from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
