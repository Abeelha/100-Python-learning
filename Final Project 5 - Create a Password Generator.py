# Theodoro Bertol Dev (Abeelha) #
# || Day 5 of #100DaysOfCode || #

#imports
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_letters = []
list_symbols = []
list_numbers = []

#Generates individual lists with random indexes
for letter in range(nr_letters):
    letters_int = random.randrange(nr_letters)
    list_letters.extend(letters[letters_int])

for symbol in range(nr_symbols):
    symbols_int = random.randrange(nr_symbols)
    list_symbols.extend(symbols[symbols_int])

for number in range(nr_numbers):
    number_int = random.randrange(nr_numbers)
    list_numbers.extend(numbers[number_int])

#Shuffleling lists to full password into 1 list
full_password = []
full_password = list_letters + list_symbols + list_numbers
random.shuffle(full_password)

password_string = ""
for word in full_password:
    password_string += str(word) + ""

#Outputs
# print (list_letters) 
# print (list_symbols)
# print (list_numbers)
print(password_string)
    