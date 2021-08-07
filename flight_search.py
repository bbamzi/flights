import requests
import os
from datetime import datetime , timedelta
ENDPOINT = 'http://tequila-api.kiwi.com/v2/search'
today = datetime.now().date()
calc = today + timedelta(days = 30 * 6)
six_month= calc.strftime('%d/%m/%y')

kiwi_apikey = os.environ.get('kiwi_apikey')

HEADER = {'apikey':kiwi_apikey}

class FlightSearch:
    def __init__(self,city):
        self.city = city
        self.PARAMETERS = {

            'fly_from': 'STN',
            'fly_to': self.city,
            'date_from': today,
            'date_to': '30/01/2022'
        }
        self.response  = requests.get(url=ENDPOINT,params=self.PARAMETERS, headers=HEADER).json()



# sea = FlightSearch('PAR')
# print(sea.response)
# print(kiwi_apikey)