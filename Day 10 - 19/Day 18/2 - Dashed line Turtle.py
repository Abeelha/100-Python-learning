# Theodoro Bertol Dev (Abeelha) #
# || Day 18 of #100DaysOfCode || #

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("DarkSlateBlue")

for _ in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    
screen = t.Screen()
screen.exitonclick()
    