# Theodoro Bertol Dev (Abeelha) #
# || Day 26 of #100DaysOfCode || #

with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 26/file1.txt") as file1:
    list1 = file1.readlines()
    
with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 26/file2.txt") as file2:
    list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]

# Write your code above 👆
print(result)