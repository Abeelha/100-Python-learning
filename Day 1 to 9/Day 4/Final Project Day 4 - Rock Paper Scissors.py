# Theodoro Bertol Dev (Abeelha) #
# || Day 4 of #100DaysOfCode || #

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_input = input("Rock, paper, or scissors?:")

player_input_low = player_input.lower()

# computer_int = random.randint(1, 3)
computer_int = 3

if player_input_low == "rock":
    print("You choose Rock!")
    print(rock)
    if computer_int == 1:
        print("Computer choose Rock!")
        print(rock)
        print("Its a Draw!")
    elif computer_int == 2:
        print("Computer choose Paper!")
        print(paper)
        print("You Lose!")
    elif computer_int == 3:
        print("Computer choose Scissors!")
        print(scissors)
        print("You Win!")
if player_input_low == "paper":
    print("You choose paper!")
    print(paper)
    if computer_int == 1:
        print("Computer choose Rock!")
        print(rock)
        print("You win!")
    elif computer_int == 2:
        print("Computer choose Paper!")
        print(paper)
        print("Its a Draw!")
    elif computer_int == 3:
        print("Computer choose Scissors!")
        print(scissors)
        print("You lose!")
if player_input_low == "scissors":
    print("You choose scissors!")
    print(scissors)
    if computer_int == 1:
        print("Computer choose Rock!")
        print(rock)
        print("You lose!")
    elif computer_int == 2:
        print("Computer choose Paper!")
        print(paper)
        print("You win!")
    elif computer_int == 3:   
        print("Computer choose Scissors!")
        print(scissors)
        print("Its a Draw!")
