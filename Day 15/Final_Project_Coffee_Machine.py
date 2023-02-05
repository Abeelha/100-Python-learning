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


def calculate_money(money: dict[str, int]):
    """Counts how much money was inputed

    Args:
        money (dict[str, int]): Dictionary containing quarters, dimes, nickles and pennies

    Returns:
        Float: Value of total money inputed
    """
    value  = 0.0
    value  += money["quarters"] * 0.25
    value  += money["dimes"] * 0.10
    value  += money["nickles"] * 0.05
    value  += money["pennies"] * 0.01

    # print(f"{value}")
    return value


def resource_cost(coffee: str):
    """Decreases the resources based of the coffee choosen

    Args:
        coffee (str): coffe chosen, each has it cost of resources
    """
    if coffee in MENU:
        for resource in resources:
            if resources[resource] >= MENU[coffee]["ingredients"][resource]:
                resources[resource] -= MENU[coffee]["ingredients"][resource]
            else:
                print(f"Sorry, there is not enough {resources[resource]} 😢")
                return False
        return True
    else:
        return False

def coffee(input: str, money: float):
    """This is the main function of the project, putting together every function to work

    Args:
        input (str): User can put any coffe, or "off" to turn off, "report" to see current resources of the coffee machine
        money (float): How much money is calculated using the calculate_money() function, but its called inside this coffe()
    """
    storaged_money = 0.0
    if input in MENU:
        cost = MENU[input]["cost"]
        if resource_cost(input)  and money >= cost:
            change = round(money - cost, 2)
            storaged_money += cost
            clear_screen()
            print(art.coffee)
            print(f"\nHere is ${change} in change.")
            print(f"\nHere is your {input} ☕")
        elif resource_cost(input) and money < cost:
            clear_screen()
            print(f"Sorry but the money you inserted: ${money}, is not enough to buy the {input} 😢\nMoney Refunded.")
        elif not resource_cost(input):
            resource_cost(input)
    elif input == "report":
        clear_screen()
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${storaged_money}')
    elif input == "off":
        sys.exit()
    else:
        clear_screen()
        print(f"\nInvalid input! '{input}'")

enought_resources = True

print(art.logo)
while enought_resources:
    buy_coffee = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if buy_coffee == "off":
        money_inputed = 0
        coffee(buy_coffee, money_inputed)
    elif buy_coffee == "report":
        money_inputed = 0
        coffee(buy_coffee, money_inputed)
    else:
        quarters = int(input("How many quarters🪙: "))
        dimes = int(input("How many dimes🪙: "))
        nickles = int(input("How many nickels🪙: "))
        pennies = int(input("How many pennies🪙: "))
        money = {
            "quarters": quarters,
            "dimes": dimes,
            "nickles": nickles,
            "pennies": pennies
        }
        money_inputed = calculate_money(money)
        coffee(buy_coffee, money_inputed)



# def coffee(input: str, money: float):
#     """This is the main function of the project, putting together every function to work

#     Args:
#         input (str): User can put any coffe, or "off" to turn off, "report" to see current resources of the coffee machine
#         money (float): How much money is calculated using the calculate_money() function, but its called inside this coffe()
#     """
#     cost = MENU[input]["cost"]
#     storaged_money = 0.0
#     if resource_cost(input) and input in MENU and money > cost:
#         change = abs(round(cost - money, 2))
#         storaged_money += cost
#         clear_screen()
#         print(art.coffee)
#         print(f"\nHere is ${change} in change.")
#         print(f"\nHere is your {input} ☕")
#     elif resource_cost(input) and input in MENU and money == cost:
#         storaged_money += cost,
#         clear_screen()
#         print(art.coffee)
#         print(f"\nThe money inserted is exactly the price of the {input}!")
#         print(f"\nHere is your {input} ☕")
#     elif resource_cost(input) and input in MENU and money < cost:
#         clear_screen()
#         print(f"Sorry but the money you inserted: ${money}, is not enought to buy the {input} 😢\nMoney Refunded.")
#         sys.exit()
#     elif not resource_cost(input):
#         resource_cost(input)
#     elif input == "report":
#         clear_screen()
#         print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${storaged_money}')
#     elif input == "off":
#         sys.exit()


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
#         nickles = int(input("How many nickles🪙: "))
#         pennies = int(input("How many pennies🪙: "))
#         money = {
#             "quarters": quarters,
#             "dimes": dimes,
#             "nickles": nickles,
#             "pennies": pennies
#         }
#         money_inputed = calculate_money(money)
#         coffee(buy_coffee, money_inputed)
        


