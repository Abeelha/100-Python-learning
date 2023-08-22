# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from twilio.rest import Client
from dotenv import load_dotenv

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.ACCOUNT_SID = os.getenv("day39_account_sid")
        self.AUTH_TOKEN = os.getenv("day39_auth_token")
        self.WHATS_API_URL = os.getenv("day39_WHATS_API")
        self.FROM_WHATS = os.getenv("day39_from_whats")
        self.TO_WHATS = os.getenv("day39_to_whats")

        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def send_notification(self, message_body):
        message = self.client.messages.create(
            from_=self.FROM_WHATS,
            body=message_body,
            to=self.TO_WHATS # type: ignore
        )
        return message.sid
    
    

# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     import os
#     import requests
#     from twilio.rest import Client
#     from dotenv import load_dotenv, dotenv_values
#     load_dotenv()

#     ACCOUNT_SID = os.getenv("day39_account_sid")
#     AUTH_TOKEN = os.getenv("day39_auth_token")
#     WHATS_API_URL = os.getenv("day39_WHATS_API")
#     FROM_WHATS = os.getenv("day39_from_whats")
#     TO_WHATS = os.getenv("day39_to_whats")
#     print(TO_WHATS)

#     auth_token = AUTH_TOKEN
#     client = Client(ACCOUNT_SID, AUTH_TOKEN)

#     message = client.messages.create(
#         from_=FROM_WHATS,
#         body='Your appointment is coming up on July 21 at 3PM1111',
#         to=TO_WHATS
#     )

#     print(message.sid)
    
#     pass
