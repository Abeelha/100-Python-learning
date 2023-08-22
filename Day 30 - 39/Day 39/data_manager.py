# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
    
import os
import requests
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class DataManager:
    def __init__(self):
        self.GET_ENDPOINT_SHEETY = os.getenv("day39_GET_ENDPOINT_SHEETY")
        self.PUT_ENDPOINT_SHEETY = os.getenv("day39_PUT_ENDPOINT_SHEETY")
        self.HEADER_AUTH_SHEETY = os.getenv("day39_HEADER_SHEETY")
        self.destination_data = {}
        
        if self.GET_ENDPOINT_SHEETY is None or self.HEADER_AUTH_SHEETY is None:
            raise ValueError("Environment variables are not set.")

    def get_destination_data(self):
        try:
            response_get = requests.get(url=self.GET_ENDPOINT_SHEETY, headers={"Authorization": self.HEADER_AUTH_SHEETY}) # type: ignore
            if response_get.status_code == 200:
                data = response_get.json()
                self.destination_data = data["prices"]
                # pprint(data)
                return self.destination_data
            else:
                print("Request failed with status code:", response_get.status_code)

        except requests.RequestException as e:
            print("Request error:", e)

    def update_destination_codes(self):
        try:
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
                        headers={"Authorization": self.HEADER_AUTH_SHEETY}
                    )
                    print(response.text)
            else:
                print("No destination data to update.")
        except requests.RequestException as e:
            print("Request error:", e)