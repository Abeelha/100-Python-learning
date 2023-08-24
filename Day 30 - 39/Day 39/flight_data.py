# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
#NOTE MY FREE API TRIAL HAS ENDED, UNFORTUNATELY I CANT TEST THE CODE </3 :( 

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