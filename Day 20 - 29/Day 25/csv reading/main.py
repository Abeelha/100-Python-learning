# Theodoro Bertol Dev (Abeelha) #
# || Day 25 of #100DaysOfCode || #

import csv
with open("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/csv reading/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
        print(row)
    temperatures.pop(0)
    for i in range(len(temperatures)):
        temperatures[i] = int(temperatures[i])
    print(temperatures)
    