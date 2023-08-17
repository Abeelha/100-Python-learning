# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from pprint import pprint
import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    
    response_get = requests.get(url=GET_ENDPOINT_SHEETY)
    
    
    json_data = response_get.json()
    
    for prices in json_data["prices"]:
        sheet_data = {
            "price": prices["Lowest Price"],
        }

    
    pprint(response_get)
    pass