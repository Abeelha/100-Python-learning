# Theodoro Bertol Dev (Abeelha) #
# || Day 13 of #100DaysOfCode || #

############DEBUGGING#####################
# Uncomment the codes below one by one to check :D

# Describe Problem
#The bug was "range(1, 20)" that the i was never going to get to 20, so i changed to 21
# def my_function():
#   for i in range(1, 21): 
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # dice_num = 6 (The bug is when randint {was: randint(1, 6)}  was 6 it goes out of index) of the dice_imgs
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: #The bug was the elif statement ( year > 1994 ), the correct is (>=)
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? ")) # The erro was str input. so i put int() so the IF statement work
# if age >= 18:
#     print(f"You can drive at age {age}.")
# else: #added else statement so it print if under 18 yrs
#     print("You can't drive, sorry")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) #The bugg was that the word_per_page was getting "==" instead of "=" 
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) #Bug was ident code, it was getting only the item and multiplying by 2, insted of appendig to the list
#   print(b_list)

# mutate([1,2,3,5,8,13])