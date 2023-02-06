# Theodoro Bertol Dev (Abeelha) #
# || Day 16 of #100DaysOfCode || #

# import platform
# import os
import art
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#IF want to clear terminal, here is the function bellow:
# def clear_screen():
#     if platform.system() == "Windows":
#         os.system("cls")
#     else:
#         os.system("clear")


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print(art.logo)
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"​What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            print(art.coffee)
            coffee_maker.make_coffee(drink)