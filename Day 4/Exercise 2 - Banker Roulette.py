# Theodoro Bertol Dev (Abeelha) #
# || Day 4 of #100DaysOfCode || #

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

len_names = len(names)
random_bill = random.randint(0, len_names)

print(f"{names[random_bill]} is going to buy the meal today!")