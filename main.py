from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
#data mgr
data_mgr = DataManager()
cities_to_check = data_mgr.city_getter()
prices_to_check = data_mgr.price_lister()

print(cities_to_check)

#


for i in range(len(cities_to_check)):
    flight_search = FlightSearch(cities_to_check[i])
    flight_data = FlightData(cities_to_check[i])

    if flight_data.air_fare < prices_to_check[i]:
        message = f"Hi, i've found a fair price for {flight_data.final_destination_city} with " \
                  f"total travel time of {flight_data.total_travel_time()} if you're interested in " \
                  f"booking, check this link out: {flight_data.deep_link_shortener()}"
        notification_manager = NotificationManager('+2348080415982',message)


