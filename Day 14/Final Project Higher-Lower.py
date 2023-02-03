# Theodoro Bertol Dev (Abeelha) #
# || Day 14 of #100DaysOfCode || #

import art
import game_data
import random
import platform
import os

score = 0

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

selected_persons = set()
def pick_random():
    """Picks 2 random dictionaries from game_data.data and put them into a list"""
    persons = []   
    for i in range(2):
        persons.append(random.choice(game_data.data))
    return persons 

def compare_followers(list_persons, guess):
    """Compare if the guess of the player is valid, count scores and return boolean if user is right"""
    global score
    # in position 0, it will be the A option for the user, and "1" option B
    if (list_persons[0]['follower_count']) > (list_persons[1]['follower_count']) and guess == "A":
        score += 1
        list_persons[1] = random.choice(game_data.data)
        clear_screen()
        print(art.logo)
        print(f"You're right! Current Score: {score}")
        return True
    elif (list_persons[0]['follower_count']) < (list_persons[1]['follower_count']) and guess == "B":
        score += 1
        list_persons[0] = list_persons[1]
        list_persons[1] = random.choice(game_data.data)
        clear_screen()
        print(art.logo)
        print(f"You're right! Current Score: {score}")
        return True
    else:
        clear_screen()
        print(art.logo)
        print(f"Sorry, That's wrong. Final Score: {score}")
        return False

def play_game():
    play = True
    while play:
        print(f"Compare A: {persons[0]['name']}, a {persons[0]['description']}, from {persons[0]['country']}.")
        print(f"Psst, testing here, the value of A is {persons[0]['follower_count']}")
        print(art.vs)
        print(f"Against B: {persons[1]['name']}, a {persons[1]['description']}, from {persons[1]['country']}.")
        print(f"Psst, testing here, the value of A is {persons[1]['follower_count']}")
        
        user_guess = input("    Who has more followers? Type 'A' or 'B': ").upper()
        result = compare_followers(persons,user_guess)
        if not result:
            play = False

print(art.logo) 
persons = pick_random()
#Starts game
play_game()

#============= Tried to make the funcion not make duplicate choices from random.. but didnt work properly :( =============
# def pick_random():
#     """Picks 2 random dictionaries from game_data.data and put them into a list"""
#     persons = []   
#     for i in range(2):
#         while True:
#             person = random.choice(game_data.data)
#             if str(person) not in selected_persons:
#                 persons.append(person)
#                 selected_persons.add(str(person))
#                 break
#     return persons

# def compare_followers(list_persons, guess):
#     """Compare if the guess of the player is valid, count scores and return boolean if user is right"""
#     global score
#     used_dicts = set()
#     # in position 0, it will be the A option for the user, and "1" option B
#     if (list_persons[0]['follower_count']) > (list_persons[1]['follower_count']) and guess == "A":
#         score += 1
#         while True:
#             new_dict = random.choice(game_data.data)
#             if str(new_dict) not in used_dicts:
#                 list_persons[1] = new_dict
#                 used_dicts.add(str(new_dict))
#                 break
#         clear_screen()
#         print(art.logo)
#         print(f"You're right! Current Score: {score}")
#         return True
#     elif (list_persons[0]['follower_count']) < (list_persons[1]['follower_count']) and guess == "B":
#         score += 1
#         used_dicts.add(str(list_persons[0]))
#         while True:
#             new_dict = random.choice(game_data.data)
#             if str(new_dict) not in used_dicts:
#                 list_persons[1] = new_dict
#                 used_dicts.add(str(new_dict))
#                 break
#         clear_screen()
#         print(art.logo)
#         print(f"You're right! Current Score: {score}")
#         return True
#     else:
#         clear_screen()
#         print(art.logo)
#         print(f"Sorry, That's wrong. Final Score: {score}")
#         return False 