# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
    
import os
import requests
import pprint
from dotenv import load_dotenv, dotenv_values
load_dotenv()

ENDPOINT_SHEETY = os.getenv("day39_ENDPOINT_SHEETY")
# HEADER_AUTH_SHEETY = os.getenv("day39_HEADER_SHEETY")

# headers_sheets = {
#     "Authorization": HEADER_AUTH_SHEETY,
# }
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response_get = requests.get(url=ENDPOINT_SHEETY) # type: ignore
        data = response_get.json()
        # pprint.pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT_SHEETY}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
    # def update_destination_codes(self):
    #     if destination_data := self.get_destination_data():
    #         for city in self.destination_data:
    #             new_data = {
    #                 "price": {
    #                     "iataCode": city["iataCode"]
    #                 }
    #             }
    #             response = requests.put(
    #                 url = f"{ENDPOINT_SHEETY}/{city['id']}",
    #                 json = new_data
    #             )
    #             print(f"{ENDPOINT_SHEETY}/{city['id']}")
    #             print(response.text)
    #     else:
    #         print("No destination data to update.")
