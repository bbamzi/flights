from flight_search import FlightSearch
import pyshorteners

ACCESS_TOKEN = '8a468945cbbc0457ba86a4fb9c1dc5d4ae42e544'

class FlightData(FlightSearch):
    #This class is responsible for structuring the flight data.

    def __init__(self, city):
        super().__init__(city)
        self.city = city
        self.data = self.response['data'][0]
        self.initial_departure_city = self.data['cityFrom']
        self.initial_departure_time = self.data['local_departure'].split('T')[1][:-8]
        self.final_destination_city =self.data['cityTo']
        self.final_destination_country = self.data['countryTo']['name']
        self.lay_over = self.data['route'][0]['cityTo']
        self.seats_left = self.data['availability']['seats']
        self.link = self.data['deep_link']
        self.airprice = self.data['price']
        self.baggage_cost = self.data['bags_price']['1']
        self.cabin_bag_cost = self.data['bags_price']
        self.final_destination_arrival_date = self.data['local_arrival'].split('T')[0]
        self.final_destination_arrival_time = self.data['local_arrival'].split('T')[1][:-8]
        self.arrival_at_stopover = self.data['route'][1]['local_arrival'].split('T')[1][:-8]
        self.layover_departure = self.data['route'][1]['local_departure'].split('T')[1][:-8]


        # self.departure_from_stopover = self.data[]



    def total_travel_time(self):
        total_travel_time = self.data['duration']['total']
        time_travelled = f'{round(total_travel_time / 3600)}:{str(total_travel_time % 3600)[:-2]}'
        return time_travelled

    def ifbagmorethan20(self):
        total = self.airprice + self.baggage_cost
        return total

    def deep_link_shortener(self):
        s = pyshorteners.Shortener(api_key=ACCESS_TOKEN)
        result = s.bitly.short(self.link)
        return result








#
#     def layover_calculator(self):
#
#
#
#
#
# flight = FlightSearch('PAR').response['data'][0]
#
#
# departure_city = flight['cityFrom']
# departure_time = flight['local_departure'].split('T')[1][:-8]
# destination_city = (flight['cityTo'])
# destination_country = flight['countryTo']['name']
# stop_overs = flight['route'][0]['cityTo']
# seat_availability = flight['availability']
# total_time_travel = flight['duration']['total']
# price = flight['price']
# handbag_weight_limit = flight['baglimit']['hand_weight']
# bag_weight_limit = flight['baglimit']['hold_weight']
# checking_bag_price = flight['bags_price']['1']
# arrival_date = flight['local_arrival'].split('T')[0]
# arrival_time = flight['local_arrival'].split('T')[1][:-8]
# layover_arrival_time =  flight['route'][0]['local_arrival'].split('T')[1][:-8]
# # LAYOVER =
# #
# #
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
# print('layover arrival time :',layover_arrival_time)
# print(flight)

fligt = FlightData('PAR')
print(fligt.data)
print(fligt.layover_departure)
print(fligt.deep_link_shortener())