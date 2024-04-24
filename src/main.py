# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# Use sheety API to get city data in Google Sheet.
cities_info = DataManager.GetCityInfo()
print(cities_info)

# Use SearchCityCode of FlightSearch to search for code of city if it's empty.
for row in cities_info:
    try:
        row['iataCode']
    except KeyError:
        city_name = row['city']
        city_code = FlightSearch.SearchCityCode(city_name)
        row['iataCode'] = city_code

# Use sheety API to update the city code on the Google Sheet.
DataManager.UpdateCityCode(cities_info)

# Search for the flight prices from one city to all the destinations in the Google Sheet and collect the result.
from_city = "London"
from_city_code = city_code = FlightSearch.SearchCityCode(from_city)
tomorrow = datetime.now() + timedelta(days=1)
date_from = tomorrow.strftime("%d/%m/%Y")
six_months_from_tomorrow = datetime.now() + timedelta(days=(6 * 30))
date_to = six_months_from_tomorrow.strftime("%d/%m/%Y")
for city in cities_info:
    to_city_code = city["iataCode"]
    flights_data = FlightSearch.SearchFlight(from_city_code, to_city_code, date_from, date_to)
    for flight in flights_data:
        from_airport = flight["flyFrom"]
        to_airport = flight["flyTo"]
        dep_time = flight["local_departure"].split("T")[1].split(".")[0] # Only extract the time.
        arr_time = flight["local_arrival"].split("T")[1].split(".")[0] # Only extract the time.
        price = flight["price"]
        try:
            city["flight"]
        except KeyError:
            city["flight"] = []
        finally:
            city["flight"].append(
                {
                    "fromAirport": from_airport,
                    "toAirport": to_airport,
                    "departureTime": dep_time,
                    "arrivalTime": arr_time,
                    "price": price
                }
            )

