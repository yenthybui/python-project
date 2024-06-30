import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
verified_number = os.environ.get("TWILIO_VERIFIED_NUMBER")

class NotificationManager:
    def __init__(self, price, departure, arrival, start_date, end_date, carrier) -> None:
        self.price = price
        self.departure = departure
        self.arrival = arrival
        self.start_date = start_date
        self.end_date = end_date
        self.carrier = carrier
    
    def send_message(self):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Low price alert! Only CAD{self.price} to fly from {self.departure} to {self.arrival}, on {self.start_date} until {self.end_date} via {self.carrier}',
            from_=virtual_number,
            to=verified_number
        )

        print(message.status)
        print(message.sid)