# Theodoro Bertol Dev (Abeelha) #
# || Day 40 of #100DaysOfCode || #

import sheety

print("Welcome to Abeelha Flight CLub. \n We find the best flight deals and email them to you.")

first_name = input("What is your First Name? ")
last_name = input("What is your Last Name? ")

email1 = "email@email.com1"
email2 = "email@email.com2"

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() in ["quit", "exit"]:
        exit()
    email2 = input("What is your email? ")
    if email2.lower() in ["quit", "exit"]:
        exit()
    
print("OK, You re in the club!")

sheety.post_new_row(first_name, last_name, email1)