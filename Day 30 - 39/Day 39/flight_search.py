# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
import requests
from dotenv import load_dotenv, dotenv_values
from data_manager import DataManager

load_dotenv()


TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
API_KEY_TEQUILA = os.getenv("day39_APIKEY_Tequila")

originBR = "SAO"
header_key = {
    "apikey" : API_KEY_TEQUILA
}

class FlightSearch:
    def get_destination_code(self, city_name):
        query = {
        "term": city_name,
        "location_types": "city"
        }
        response = requests.get(
            url = f"{TEQUILA_ENDPOINT}/locations/query", #type:ignore
            headers = header_key, #type:ignore
            params = query
        )
        # print(response.text)
        results = response.json()["locations"]
        return results[0]["code"]