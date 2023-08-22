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

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    
# data_manager = DataManager()
# if lowest_prices := data_manager.get_lowest_prices():
#     notification_manager = NotificationManager()
#     message = "Lowest prices: " + ", ".join(map(str, sheet_data))
#     message_sid = notification_manager.send_notification(message)
#     print("Notification sent with message SID:", message_sid)
# else:
#     print("No lowest prices found.")