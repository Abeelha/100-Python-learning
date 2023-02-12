# Theodoro Bertol Dev (Abeelha) #
# || Day 12 of #100DaysOfCode || #


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#imports
import random
from art import logo

#Global variables:
choice_made = True
random_number = random.randint(1,100)

def check_number(guess, lives):
    """Checks if the player input was the number random generated"""
    global random_number
    while lives > 0:
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        elif guess < random_number:
            lives -= 1
            guess = int(input(f"\nToo Low!\nYou have {lives} attempts remaining to guess the number.\n    Guess again: "))
        elif guess > random_number:
            lives -= 1
            guess = int(input(f"\nToo High!\nYou have {lives} attempts remaining to guess the number.\n    Guess again: "))
    #IDK why, but it prints "You have  0 Attempts remaining hahaha, but anyway, its working at least :D"
    else:
        print("You lose.")

#Logo display:
print(logo)
#User Chooses dificulty
hard_or_easy = input("\nWelcome to the Number Guessing Game!\n    I'm Thinking of a number between 1 and 100.\n    Choose a difficulty. Type 'easy or 'hard': ").lower()

#Test code:
print(f"\nPsst, the correct answer is {random_number}")

if hard_or_easy == "easy":
    #Easy mode gets 10 attempts
    lives_easy = 10
    guess = int(input("You have 10 attempts remaining to guess the number.\n    Make a guess: "))
    check_number(guess=guess, lives=lives_easy)
elif hard_or_easy == "hard":
    #Hard mode gets 5 attempts
    lives_hard = 5
    guess = int(input("You have 5 attempts remaining to guess the number.\n    Make a guess: "))
    check_number(guess=guess, lives=lives_hard)
else:
    print("You did not type correctly, try again typing 'Easy' or 'Hard'")