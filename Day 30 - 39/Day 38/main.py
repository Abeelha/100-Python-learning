# Theodoro Bertol Dev (Abeelha) #
# || Day 38 of #100DaysOfCode || #

import requests
import datetime

#Create account and get ur ID and APIKEY here: https://developer.nutritionix.com
APP_ID = "f9f78bec"
API_KEY = "9b736f8c0c82378953bd4764247737a8"
ENDPOINT_EXERCISE = "https://trackapi.nutritionix.com/v2/natural/exercise"
ENDPOINT_SHEETY = "https://api.sheety.co/7e1fc263972ddfa7d19da8424cfaca11/myWorkouts/workouts"
AUTH = "Basic QWJlZWxoYTphYmFjYXRlNDMyMQ=="
GENDER = "Male"
WEIGHT_KG = 70
HEIGHT_CM = 1.82
AGE = 21

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract the day and time components
current_day = current_datetime.strftime("%d/%m/%Y")  # Full weekday name
current_time = current_datetime.strftime("%X")  # 24-hour format

headers_exercise = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
headers_sheets = {
    "Authorization": AUTH,
}
body_exercises = {
    "query": input("What exercise did you do today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

#Test GET SHEETY
# response = requests.get(url=ENDPOINT_SHEETY,headers=headers_sheets)

response_exercise = requests.post(url=ENDPOINT_EXERCISE, json=body_exercises, headers=headers_exercise)
# print(response.text)

# Response filter
json_data = response_exercise.json()

for exercise in json_data["exercises"]:
    body_add_row_sheety = {
        "workout": {
            "date": current_day,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response_sheety = requests.post(url=ENDPOINT_SHEETY, json=body_add_row_sheety)
    print(response_sheety.text)

# for exercise in json_data["exercises"]:
#     exercise_name = exercise["name"].title()
#     duration_minutes = exercise["duration_min"]
#     calories_burned = exercise["nf_calories"]
    
# body_add_row_sheety = {
#     "workout": {
#         "Date" : current_day,
#         "Time" : current_time,
#         "Exercise" : exercise_name,
#         "Duration" : duration_minutes,
#         "Calories" : calories_burned,
#     }
# }

# if response.status_code == 200:
# else:
#     print(f"Request failed with status code: {response.status_code}")