from flight_search import FlightSearch
import pyshorteners

ACCESS_TOKEN = '8a468945cbbc0457ba86a4fb9c1dc5d4ae42e544'


class FlightData(FlightSearch):
    # This class is responsible for structuring the flight data.

    def __init__(self, city):
        super().__init__(city)
        self.city = city
        self.data = self.response['data'][0]
        self.initial_departure_city = self.data['cityFrom']
        self.initial_departure_time = self.data['local_departure'].split('T')[1][:-8]
        self.final_destination_city = self.data['cityTo']
        self.final_destination_country = self.data['countryTo']['name']
        self.lay_over = self.data['route'][0]['cityTo']
        self.seats_left = self.data['availability']['seats']
        self.link = self.data['deep_link']
        self.air_fare = self.data['price']
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
        total = self.air_fare + self.baggage_cost
        return total

    def deep_link_shortener(self):
        s = pyshorteners.Shortener(api_key=ACCESS_TOKEN)
        result = s.bitly.short(self.link)
        return result



