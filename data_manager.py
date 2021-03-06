import requests

ENDPOINT = 'https://api.sheety.co/52e86d174bef040c09cfc3a9a49ea464/flightDeals/prices'
PARAMETERS = {}


class DataManager:
    def __init__(self):
        self.response = requests.get(ENDPOINT).json()

    def city_getter(self):
        city_list = []
        for i in self.response['prices']:
            city_list.append(i['iataCode'])
        return city_list

    def price_lister(self):
        price_list = []
        for i in self.response['prices']:
            price_list.append(i['lowestPrice'])
        return price_list

dt = DataManager()

print(dt.price_lister())
