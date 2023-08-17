# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class FlightData:
    #This class is responsible for structuring the flight data.
    SEARCH_ENDPOINT_KIWI = "https://api.tequila.kiwi.com/v2/search"
    originBR = "SAO"
    destinationCA = "YTO"
    flight_data = {
        # "apikey": APIKEY,
        "fly_from": originBR,
        "fly_to" : destinationCA
    }
    pass