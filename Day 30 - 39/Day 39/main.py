# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
#NOTE MY FREE API TRIAL HAS ENDED, UNFORTUNATELY I CANT TEST THE CODE </3 :( 

import os
from pprint import pprint
from datetime import datetime, timedelta
from dotenv import load_dotenv, dotenv_values
load_dotenv()

#Imported files
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

#Getting date/time
tomorrow_day = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "SAO"

#Searching IATA code based on google sheet City names
for row_index, row in enumerate(sheet_data[:15], start=1):  # Loop through the first 15 rows
    if row["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()
    
#Getting data from destination based on previous IATA code we got   
for destination in sheet_data:
    flight = flight_search.search_travel(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow_day,
        to_time=six_month_from_today
    )
    #Sending notification in whatsapp of lowest prices
    if flight.price < destination["lowestPrice"]:  #type:ignore
        notification_manager.send_notification(message=f"Low price alert! Only BRL{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")  #type:ignore