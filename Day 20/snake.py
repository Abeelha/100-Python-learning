# Theodoro Bertol Dev (Abeelha) #
# || Day 20 of #100DaysOfCode || #

#Imports
from turtle import Turtle
#Const
STARTING_POSITIONS =[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Main class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Creates snake
    def create_snake(self):    
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    #Move snakle
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    #Move snake UP
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    #Move snake Down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    #Move snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    #Move snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)