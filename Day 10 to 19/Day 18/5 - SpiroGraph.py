# Theodoro Bertol Dev (Abeelha) #
# || Day 18 of #100DaysOfCode || #

import turtle as t
import random

tim = t.Turtle()
tim.width(2)
tim.speed("fastest")


t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b
    

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        rotation = tim.heading()
        tim.circle(150)
        tim.setheading(rotation + size_of_gap)
        tim.color(random_color())

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

