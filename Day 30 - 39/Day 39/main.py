# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

import requests
from pprint import pprint

#Imported files
from data_manager import DataManager
from notification_manager import NotificationManager
# from flight_data import FlightData
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
