# Theodoro Bertol Dev (Abeelha) #
# || Day 7 of #100DaysOfCode || #

import random
import HangMan_art
import HangMan_Words
import os


#variables and random word picking
end_of_game = False
chosen_word = random.choice(HangMan_Words.word_list)
word_length = len(chosen_word)
display = []
letters_guessed= []
lives = 6

#create display depending the lenght of the random word 
for letter in chosen_word:
    display += "_"

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Logo
print(HangMan_art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Clear terminal for better viewing
    os.system('cls')

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letters_guessed:
        print(f"You already guessed that letter! '{guess}'")
    else:
        letters_guessed.append(guess)
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word! You lose a life")
        #Then reduce 'lives' by 1. 
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(HangMan_art.stages[lives])

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives <= 0:
        end_of_game = True
        print("You Lose!")