# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
    
import os
import requests
import pprint
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class DataManager:
    def __init__(self):
        self.GET_ENDPOINT_SHEETY = os.getenv("day39_GET_ENDPOINT_SHEETY")
        self.PUT_ENDPOINT_SHEETY = os.getenv("day39_PUT_ENDPOINT_SHEETY")
        self.HEADER_AUTH_SHEETY = os.getenv("day39_HEADER_SHEETY")
        self.headers_sheets = {
            "Authorization": self.HEADER_AUTH_SHEETY,
        }
        self.destination_data = {}

    def get_destination_data(self):
        response_get = requests.get(url=self.GET_ENDPOINT_SHEETY, headers=self.headers_sheets) # type: ignore
        data = response_get.json()
        # pprint.pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        if destination_data := self.get_destination_data():
            for city in self.destination_data:
                new_data = {
                    "price": {
                        "iataCode": city["iataCode"]
                    }
                }
                response = requests.put(
                    url = f"{self.PUT_ENDPOINT_SHEETY}/{city['id']}",
                    json = new_data,
                    headers=self.headers_sheets # type: ignore
                )
                print(response.text)
        else:
            print("No destination data to update.")
