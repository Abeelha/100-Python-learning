# Theodoro Bertol Dev (Abeelha) #
# || Day 21 of #100DaysOfCode || #

#Imports
from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Snake setup
snake = Snake()

#Food setup
food = Food()

#Scoreboard setup
scoreboard = Scoreboard()

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
    
    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()        
        scoreboard.increase_score()
    
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collision with tail
        #if head collides with any segment in the tail
            #trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

#Exit screen when clicking
screen.exitonclick()