# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv, dotenv_values
from data_manager import DataManager
from pprint import pprint

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
API_KEY_TEQUILA = os.getenv("day39_APIKEY_Tequila")

header_key = {
    "apikey" : API_KEY_TEQUILA
}

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    # def flight_data(self, IATA_code):
    #     # You can use the split() function to get the first part of the date from the API response.
        
    #     # Get the current date and time
    #     current_date = datetime.now()
    #     current_time = current_date.strftime("%d-%m-%Y")

    #     # Add 6 intervals of 30 days
    #     new_date_after_30_days = current_date + timedelta(days=30*6)
    #     new_date_after_30_days = new_date_after_30_days.strftime("%d-%m-%Y")

    #     # Add 6 months
    #     new_date_after_6_months = current_date.replace(month=current_date.month + 6)
    #     new_date_after_6_months = new_date_after_6_months.strftime("%d-%m-%Y")

    #     print("Current Date:", current_date)
    #     print("Date after 6 intervals of 30 days:", new_date_after_30_days)
    #     print("Date after 6 months:", new_date_after_6_months)
        
    #     query = {
    #         "fly_from": "SAO",
    #         "location_types": "city",
    #         "fly_to": IATA_code,
    #         "date_from": current_time,
    #         "date_to": new_date_after_30_days,
    #     }
        
    #     response = requests.get(
    #         url= f"{TEQUILA_ENDPOINT}/search",
    #         headers = header_key, #type : ignore
    #         params = query
    #         )
        
    #     print(response.text)