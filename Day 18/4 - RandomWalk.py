# Theodoro Bertol Dev (Abeelha) #
# || Day 18 of #100DaysOfCode || #

import turtle as t
import random

tim = t.Turtle()
tim.width(10)
tim.speed(10)


t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b
    


for _ in range(100):
    random_direc = [0,90,180,270]
    tim.forward(30)
    tim.setheading(random.choice(random_direc))

    tim.color(random_color())


screen = t.Screen()
screen.exitonclick()
