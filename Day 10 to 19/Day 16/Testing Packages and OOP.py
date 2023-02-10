# Theodoro Bertol Dev (Abeelha) #
# || Day 15 of #100DaysOfCode || #


from turtle import Turtle, Screen

# my_screen = Screen()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# Theodoro Bertol Dev (Abeelha) #
# || Day 16 of #100DaysOfCode || #

# timmy.forward(200)

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","water","Fire"])
table.align = "l"
print(table)