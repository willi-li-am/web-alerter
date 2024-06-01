import os
from dotenv import load_dotenv

from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

def sendSMS(sms: str) -> None:
    TWILIO_AUTH = os.getenv('TWILIO_AUTH')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    ACCOUNT_SID = os.getenv('ACCOUNT_SID')

    client = Client(ACCOUNT_SID, TWILIO_AUTH)

    message = client.messages.create(
        from_='+18287151987',
        body=sms,
        to=PHONE_NUMBER
    )

    print(message.sid)