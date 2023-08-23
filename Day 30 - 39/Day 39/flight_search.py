# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
import requests
from dotenv import load_dotenv, dotenv_values
from data_manager import DataManager

load_dotenv()


SEARCH_ENDPOINT_KIWI = os.getenv("TEQUILA_ENDPOINT")
API_KEY_TEQUILA = os.getenv("day39_APIKEY_Tequila")

originBR = "SAO"
header_key = {
    "apikey" : API_KEY_TEQUILA
}

class FlightSearch:
    def __init__(self):
        self.cities = []

    def get_destination_code(self, city_name):
        data_manager = DataManager()
        sheet_data = data_manager.get_destination_data()
        for row in sheet_data:
            self.cities.append(row["city"])
        print(self.cities)
            
        body_json = {
            "term" : self.cities,
            "location_types" : "country"
        }

        respose = requests.get(
            url = SEARCH_ENDPOINT_KIWI, #type:ignore
            json = body_json,
            headers = header_key #type:ignore
            )
    
# flight_data = {
#     # "apikey": APIKEY,
#     "fly_from": originBR,
#     "fly_to" : destinationCA
# }