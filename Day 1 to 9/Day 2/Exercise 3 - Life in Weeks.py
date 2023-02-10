# Theodoro Bertol Dev (Abeelha) #
# || Day 2 of #100DaysOfCode || #

age = input("What is your current age? ")

age_left = 90 - int(age)

months_left = age_left*12
weeks_left = age_left*52
days_left = age_left*365

print(f"You have {days_left} days left, {weeks_left} weeks left and {months_left} months left")