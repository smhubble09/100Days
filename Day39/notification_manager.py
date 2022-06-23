import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_text(self,message):
        sms_message = self.client.messages.create(
                body=message,
                from_= TWILIO_VIRTUAL_NUMBER,
                to= TWILIO_VERIFIED_NUMBER
            )
        print(sms_message.sid)