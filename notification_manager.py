from twilio.rest import Client

TOKEN = 'AC964a8ed0a992f34c18c7c1d6181c9afa'
AUTH = '746d28ab1dd020be9d53d5d9320f2e9c'
PHONE_NUMBER = '+13126260133'


class NotificationManager:

    def __init__(self, num):
        message = self.message_receiver('')
        self.num = num
        self.client = Client(TOKEN, AUTH)
        self.message = self.client.messages.create(
            body=message,
            from_=PHONE_NUMBER,
            to=self.num
        )

    def message_receiver(self, message):
        return message
