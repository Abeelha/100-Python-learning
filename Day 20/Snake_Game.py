# Theodoro Bertol Dev (Abeelha) #
# || Day 20 of #100DaysOfCode || #

from turtle import Screen
import time
import random
from snake import Snake

#Screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Snake setup
snake = Snake()

#Input keys to move snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#Make the game run
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Exit screen when clicking
screen.exitonclick()