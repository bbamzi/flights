from data_manager import DataManager

dt = DataManager()
cities = dt.city_getter()
print(cities)

for i in range(len(cities)):
    print(cities[i])
