from twilio.rest import Client
import os

twilio_TOKEN = os.environ.get('twilio_TOKEN')
twilio_AUTH = os.environ.get('twilio_AUTH')
PHONE_NUMBER = '+13126260133'


class NotificationManager:

    def __init__(self, num, message):
        self.num = num
        self.message = message
        self.client = Client(twilio_TOKEN, twilio_AUTH)
        self.message = self.client.messages.create(
            body=message,
            from_=PHONE_NUMBER,
            to=self.num
        )

    def message_receiver(self, message):
        return message
