# Theodoro Bertol Dev (Abeelha) #
# || Day 19 of #100DaysOfCode || #

import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_screen():
    tim.reset()
    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
