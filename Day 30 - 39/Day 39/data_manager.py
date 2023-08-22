# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

class DataManager:
    import os
    from dotenv import load_dotenv, dotenv_values
    from pprint import pprint
    import requests
    load_dotenv()

    # This class is responsible for talking to the Google Sheet.
    GET_ENDPOINT_SHEETY = os.getenv("day39_GET_ENDPOINT_SHEETY")
    # print(GET_ENDPOINT_SHEETY)
    HEADER_AUTH_SHEETY = os.getenv("day39_HEADER_SHEETY")
    # print(HEADER_AUTH_SHEETY)
    

    # Check if environment variables are set
    if GET_ENDPOINT_SHEETY is None or HEADER_AUTH_SHEETY is None:
        raise ValueError("Environment variables are not set.")
        
    try:
        # Make the GET request
        response_get = requests.get(url=GET_ENDPOINT_SHEETY, headers={"Authorization": HEADER_AUTH_SHEETY})
        # pprint(response_get.text)

        # # Check response status code
        if response_get.status_code == 200:
            json_data = response_get.json()
            
            for prices in json_data["prices"]:
                sheet_data = {
                    "price": prices["lowestPrice"],
                }
                pprint(sheet_data)
        else:
            print("Request failed with status code:", response_get.status_code)

    except requests.RequestException as e:
        print("Request error:", e)
    pass