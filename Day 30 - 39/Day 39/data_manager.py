# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

from pprint import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    GET_ENDPOINT_SHEETY = "https://api.sheety.co/7e1fc263972ddfa7d19da8424cfaca11/flightDeals/prices"
    PUT_ENDPOINT_SHEETY = "https://api.sheety.co/7e1fc263972ddfa7d19da8424cfaca11/flightDeals/prices/[Object ID]"
    
    response_get = requests.get(url=GET_ENDPOINT_SHEETY)
    
    
    json_data = response_get.json()
    
    for prices in json_data["prices"]:
        sheet_data = {
            "price": prices["Lowest Price"],
        }

    
    pprint(response_get)
    pass