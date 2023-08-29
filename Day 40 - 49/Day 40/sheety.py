# Theodoro Bertol Dev (Abeelha) #
# || Day 40 of #100DaysOfCode || #

#Imports
import os
import requests
from pprint import pprint

#Input your .env variables to work
BEARER = os.getenv('BEARER_TOKEN')
USERNAME = os.getenv('API_USERNAME_SHEETY')
PROJECT ="flightDealsUsers"
SHEET = "users"

#Base URL
base_url = "https://api.sheety.co"

#Function to post request
def post_new_row(first_name, last_name, email):

    #Headers for request
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type" : "application/json",
        }

    #Body for request
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    
    response = requests.post(url=base_url, headers=headers, json=body)
    response.raise_for_status()
    pprint(response)