import requests
from datetime import datetime , timedelta
ENDPOINT = 'http://tequila-api.kiwi.com/v2/search'
today = datetime.now().date()
calc = today + timedelta(days = 30 * 6)
six_month= calc.strftime('%d/%m/%y')


HEADER = {'apikey':'WUIz467vwCtSt8GJF08xCCiIhv0NPSpJ'}

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



flight = FlightSearch('PAR').response['data'][0]


# departure_city = flight['cityFrom']
# departure_time = flight['local_departure'].split('T')[1][:-8]
# destination_city = (flight['cityTo'])
# destination_country = flight['countryTo']['name']
# stop_overs = flight['route'][0]['cityFrom']
# seat_availability = flight['availability']
# total_time_travel = flight['duration']['total']
# price = flight['price']
# handbag_weight_limit = flight['baglimit']['hand_weight']
# bag_weight_limit = flight['baglimit']['hold_weight']
# checking_bag_price = flight['bags_price']['1']
# arrival_date = flight['local_arrival'].split('T')[0]
# arrival_time = flight['local_arrival'].split('T')[1][:-8]
# LAYOVER =
#
#
# print(flight)
# print('departure city: ',departure_city)
# print('departure time',departure_time)
# print('destination city',destination_city)
# print('destination country', destination_country)
# print('seat left',seat_availability)
# print(f'total time {round(total_time_travel / 3600)}:{str(total_time_travel % 3600)[:-2]}')
# print('handbag weight limit',handbag_weight_limit)
# print('major bag limit',bag_weight_limit)
# print('price',price)
# print('checked bag price:',checking_bag_price )
# print('destination arrival date: ',arrival_date)
# print('destination arrival time: ', arrival_time)

print(flight)
