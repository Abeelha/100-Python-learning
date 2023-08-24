# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
#NOTE MY FREE API TRIAL HAS ENDED, UNFORTUNATELY I CANT TEST THE CODE </3 :( 

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

    def send_notification(self, message):
        message = self.client.messages.create(
            from_=self.FROM_WHATS,
            body=message,
            to=self.TO_WHATS # type: ignore
        )
        return message.sid