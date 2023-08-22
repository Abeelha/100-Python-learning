# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()


class FlightSearch:
    def __init__(self,):
        TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
        TEQUILA_API_KEY = os.getenv("day39_APIKEY_Tequila")
        
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code