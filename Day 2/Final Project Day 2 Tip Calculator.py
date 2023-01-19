# Theodoro Bertol Dev (Abeelha) #
# || Day 2 of #100DaysOfCode || #

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_value_str = input("Whats the value of the bill?  ")
people_to_pay = input("How many people will split the bill?  ")
tip_input = input("do you want to tip with: 12%, 15% or 20%?  ")

bill_value_int = float(bill_value_str)
people_to_pay_int = int(people_to_pay)
tip_input_int = int(tip_input)

if tip_input_int == 12:
    bill_per_person = (bill_value_int / people_to_pay_int) *1.12
elif tip_input_int == 15:
    bill_per_person = (bill_value_int / people_to_pay_int) *1.15
elif tip_input_int == 20:
    bill_per_person = (bill_value_int / people_to_pay_int) *1.20
else:
    print("You didnt inform the correct percentage of the tip!")
bill_per_person_rounded = "{:.2f}".format(bill_per_person)

print(f"Every person needs to pay {bill_per_person_rounded}")