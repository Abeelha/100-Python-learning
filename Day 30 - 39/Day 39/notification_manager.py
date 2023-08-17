# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #
import os
from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "AC7bcdc60e5c4b5cdb08c55dd62a78348b"
    auth_token = "52328101fe6218689f5e8a2efb2c8dd2"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello there!',
        from_='whatsapp:+14155238886',
        to='whatsapp:+15005550006'
    )
    print(message.sid)
    pass