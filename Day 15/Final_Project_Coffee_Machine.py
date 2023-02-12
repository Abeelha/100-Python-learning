# Theodoro Bertol Dev (Abeelha) #
# || Day 15 of #100DaysOfCode || #

import platform
import os
import sys
import art


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


#Version 2.0, simplified code
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



#Version 1.0

# def calculate_money(money: dict[str, int]):
#     """Counts how much money was inputed

#     Args:
#         money (dict[str, int]): Dictionary containing quarters, dimes, nickles and pennies

#     Returns:
#         Float: Value of total money inputed
#     """
#     value  = 0.0
#     value  += money["quarters"] * 0.25
#     value  += money["dimes"] * 0.10
#     value  += money["nickles"] * 0.05
#     value  += money["pennies"] * 0.01

#     # print(f"{value}")
#     return value


# def resource_cost(coffee: str):
#     """Decreases the resources based of the coffee choosen

#     Args:
#         coffee (str): coffe chosen, each has it cost of resources
#     """
#     if coffee in MENU:
#         for resource in resources:
#             if resources[resource] >= MENU[coffee]["ingredients"][resource]:
#                 resources[resource] -= MENU[coffee]["ingredients"][resource]
#             else:
#                 print(f"Sorry, there is not enough {resources[resource]} 😢")
#                 return False
#         return True
#     else:
#         return False

# def coffee(input: str, money: float):
#     """This is the main function of the project, putting together every function to work

#     Args:
#         input (str): User can put any coffe, or "off" to turn off, "report" to see current resources of the coffee machine
#         money (float): How much money is calculated using the calculate_money() function, but its called inside this coffe()
#     """
#     storaged_money = 0.0
#     if input in MENU:
#         cost = MENU[input]["cost"]
#         if resource_cost(input)  and money >= cost:
#             change = round(money - cost, 2)
#             storaged_money += cost
#             clear_screen()
#             print(art.coffee)
#             print(f"\nHere is ${change} in change.")
#             print(f"\nHere is your {input} ☕")
#         elif resource_cost(input) and money < cost:
#             clear_screen()
#             print(f"Sorry but the money you inserted: ${money}, is not enough to buy the {input} 😢\nMoney Refunded.")
#         elif not resource_cost(input):
#             resource_cost(input)
#     elif input == "report":
#         clear_screen()
#         print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${storaged_money}')
#     elif input == "off":
#         sys.exit()
#     else:
#         clear_screen()
#         print(f"\nInvalid input! '{input}'")

# enought_resources = True

# print(art.logo)
# while enought_resources:
#     buy_coffee = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
#     if buy_coffee == "off":
#         money_inputed = 0
#         coffee(buy_coffee, money_inputed)
#     elif buy_coffee == "report":
#         money_inputed = 0
#         coffee(buy_coffee, money_inputed)
#     else:
#         quarters = int(input("How many quarters🪙: "))
#         dimes = int(input("How many dimes🪙: "))
#         nickles = int(input("How many nickels🪙: "))
#         pennies = int(input("How many pennies🪙: "))
#         money = {
#             "quarters": quarters,
#             "dimes": dimes,
#             "nickles": nickles,
#             "pennies": pennies
#         }
#         money_inputed = calculate_money(money)
#         coffee(buy_coffee, money_inputed)
