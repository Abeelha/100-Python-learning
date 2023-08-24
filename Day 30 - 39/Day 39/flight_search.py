# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
#NOTE MY FREE API TRIAL HAS ENDED, UNFORTUNATELY I CANT TEST THE CODE </3 :( 

import os
import requests
from dotenv import load_dotenv, dotenv_values
from data_manager import DataManager
from flight_data import FlightData

load_dotenv()


TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
API_KEY_TEQUILA = os.getenv("day39_APIKEY_Tequila")

originBR = "SAO"
header_key = {
    "apikey" : API_KEY_TEQUILA
}

class FlightSearch:
    def get_destination_code(self, city_name):
        query = {
        "term": city_name,
        "location_types": "city"
        }
        response = requests.get(
            url = f"{TEQUILA_ENDPOINT}/locations/query", #type:ignore
            headers = header_key, #type:ignore
            params = query
        )
        # print(response.text)
        results = response.json()["locations"]
        return results[0]["code"]
    
    def search_travel(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY_TEQUILA}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "BRL"
        }
        
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers, #type:ignore
            params=query,
        )
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        
        return flight_data