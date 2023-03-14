# Theodoro Bertol Dev (Abeelha) #
# || Day 34 of #100DaysOfCode || #

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
