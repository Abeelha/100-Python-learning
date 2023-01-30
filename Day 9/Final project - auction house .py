# Theodoro Bertol Dev (Abeelha) #
# || Day 8 of #100DaysOfCode || #

import os
import art

print(art.logo)

all_bids = {}

# Using lambda to create a dictionary with the person and their highest bid:
# def highest_bid_func(bids_dictionary):
    # highest_bid = max(all_bids.items(), key = lambda item: item[1])
    # print(f"The winner with the highest bid is: {highest_bid}")

#Using 2 variables to store max bid and their key in dictionary:
def highest_bid_func(bids_dictionary):
    highest_bid = max(all_bids.values())
    highest_bid_winner = max(all_bids,key = all_bids.get)

    print(f"The winner is {highest_bid_winner}, with a bid of {highest_bid}!")


choice = "yes"
while choice == "yes":
    name = input("What's your name?: ")
    bid = input("What's your bid?: ")
    bid = int(bid)
    
    all_bids[name] = bid
    
    os.system('cls')
    
    print(art.logo)
    choice = input("Are there any other bidders? Type 'yes', 'no': ").lower()
    
highest_bid_func(all_bids)