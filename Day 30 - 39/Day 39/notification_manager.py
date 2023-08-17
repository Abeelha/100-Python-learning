# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello there!',
        from_='whatsapp:+14155238886',
        to='whatsapp:+15005550006'
    )
    print(message.sid)
    pass