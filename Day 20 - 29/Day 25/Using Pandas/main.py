# Theodoro Bertol Dev (Abeelha) #
# || Day 25 of #100DaysOfCode || #
# Using the pandas library
import pandas

data = pandas.read_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/csv reading/weather_data.csv")

# print(type(data))
# print(type(data["temp"]))

# #Transforming data to list
# temp_list = data["temp"].to_list()
# #transforming data to dictionary
# data_dict = data.to_dict()

# #Get data temperature collumn
# print(data["temp"])

# #"Hard" way to make average of temp
# # average_temp = round(sum(temp_list) / len(temp_list))
# # print(average_temp)

# #Easy way to make average of temp
# print(data["temp"].mean())
# print(data["temp"].max())

# #highest temp in which day?
# print(data[data.temp == data.temp.max()])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Get Row data value
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/Using Pandas/new_data.csv")


# Central Park Squirrel Data Analysis

data = pandas.read_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/Using Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("C:/Users/Abeelha/Documents/Programs/100 Python learning/Day 25/Using Pandas/squirrel_count.csv")
