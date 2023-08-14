# Theodoro Bertol Dev (Abeelha) #
# || Day 37 of #100DaysOfCode || #

from tokenize import Token
from datetime import datetime

import requests
TOKEN = "ajdh1odsa1hj32io1"  # --- create ur token, it can be random characters ---
USERNAME = "abeelha" # --- create ur Username ---
ID_GRAPH = "code-graph" # --- create ur Graph ID ---
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_endpoint_create = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_endpoint_post = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAPH}"
graph_endpoint_edit = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAPH}/20230814"

# Get today's date
TODAY = datetime.now()

# Format the date as yyyyMMdd
formatted_date = TODAY.strftime('%Y%m%d')
# formatted_date = "20230813" #Testing with manual dateTime yyyyMMdd

headers = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_create_params = {
    "id": ID_GRAPH, #YOUR_Graph_ID_goes_here
    "name": "Coding-Theo", 
    "unit": "Mins",
    "type": "float",
    "color":"ajisai",
}

graph_post_params = {
    "date": formatted_date,
    "quantity": input("How much time(in minutes), did i studied today?: "),
    # "optionalData":"{\"Description\":\"Day 37 of 100 days of code, first commit in pixela APIs\"}"
}

graph_edit_params = {
    "quantity": "120",
    "optionalData":"{\"Description\":\"Day 37 of 100 days of code, first commit in pixela APIs(Edit quantity minutes)\"}"
}

#Creating username
# response_username = requests.post(url=pixela_endpoint, json=user_params)
# print(response_username.text)

#Creating graph
# response_graph = requests.post(url=graph_endpoint_create, json=graph_create_params, headers=headers)
# print(response_graph.text)

#To see if it worked, go to this URL and change it to accordingly
# https://pixe.la/v1/users/{YOUR_USERNAME}/graphs/{ID_Your_Graph}.html

#Post Editing data in graph
# response_graph = requests.put(url=graph_endpoint_edit, json=graph_edit_params, headers=headers)
# print(response_graph.text)

#Post inputing data in graph
response_graph = requests.post(url=graph_endpoint_post, json=graph_post_params, headers=headers)
print(response_graph.text)