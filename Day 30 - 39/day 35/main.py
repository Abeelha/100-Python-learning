# Theodoro Bertol Dev (Abeelha) #
# || Day 35 of #100DaysOfCode || #

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "55ee8994a8fde207d18ebdc98c39313c"

parameters = {
    "lat" : -26.23,
    "lon" : -52.67,
    "appid" : api_key,
    # "exclude" : "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data =response.json
print(weather_data)