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
from flight_data import FlightData
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
sheet_data = data_manager.get_destination_data()


for row_index, row in enumerate(sheet_data[:10], start=1):  # Loop through the first 10 rows
    if row["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            row["iataCode"] = flight_data.flight_data(row["code"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()
