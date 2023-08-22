# Theodoro Bertol Dev (Abeelha) #
# || Day 39 of #100DaysOfCode || #



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    import os
    import requests
    from twilio.rest import Client
    from dotenv import load_dotenv, dotenv_values
    load_dotenv()

    ACCOUNT_SID = os.getenv("day39_account_sid")
    AUTH_TOKEN = os.getenv("day39_auth_token")
    WHATS_API_URL = os.getenv("day39_WHATS_API")
    from_whats = os.getenv("day39_from_whats")
    to_whats = os.getenv("day39_to_whats")

    account_sid = 'AC7bcdc60e5c4b5cdb08c55dd62a78348b'
    auth_token = '[AuthToken]'
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+555191068594'
    )

    print(message.sid)
    
    pass