# Theodoro Bertol Dev (Abeelha) #
# || Day 13 of #100DaysOfCode || #

#Code to debug:
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
    
#Debugged code:
#Changed OR to AND, if to elif, ([number]) to (number). :)
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
