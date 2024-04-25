# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# Use sheety API to get city data in Google Sheet.
cities_info = DataManager.GetCityInfo()

# Use SearchCityCode of FlightSearch to search for code of city if it's empty.
for row in cities_info:
    try:
        row['iataCode']
    except KeyError:
        # If code is empty, find the code and update in the Google Sheet.
        city_name = row['city']
        city_code = FlightSearch.SearchCityCode(city_name)
        city_id = row["id"]
        DataManager.UpdateCityCode(city_id, city_code)
        row['iataCode'] = city_code

# Search for the flight prices from one city to all the destinations in the Google Sheet and collect the result.
from_city = "London"
from_city_code = city_code = FlightSearch.SearchCityCode(from_city)
tomorrow = datetime.now() + timedelta(days=1)
date_from = tomorrow.strftime("%d/%m/%Y")
six_months_from_tomorrow = datetime.now() + timedelta(days=(4 * 30))
date_to = six_months_from_tomorrow.strftime("%d/%m/%Y")
update_data = []
for city_info in cities_info:
    to_city_code = city_info["iataCode"]
    flights_data = FlightSearch.SearchFlight(from_city_code, to_city_code, date_from, date_to)
    if flights_data:
        for flight in flights_data:
            from_airport = flight["flyFrom"]
            to_airport = flight["flyTo"]
            dep_date = flight["local_departure"].split("T")[0]
            dep_time = flight["local_departure"].split("T")[1].split(".")[0] # Only extract the time.
            arr_date = flight["local_arrival"].split("T")[0]
            arr_time = flight["local_arrival"].split("T")[1].split(".")[0] # Only extract the time.
            price = flight["price"]
            try:
                city_info["flight"]
            except KeyError:
                city_info["flight"] = []
            finally:
                city_info["flight"].append(
                    {
                        "from_airport": from_airport,
                        "to_airport": to_airport,
                        "departure_date": dep_date,
                        "departure_time": dep_time,
                        "arrival_date": arr_date,
                        "arrival_time": arr_time,
                        "price": price
                    }
                )
        # After finding all flights, then find the cheapest flight.
        cheapest_flight = min(city_info["flight"], key=lambda x: x["price"])
        update_data.append(
            {
                "city": city_info["city"],
                "id": city_info["id"],
                "cheapest_flight": cheapest_flight
            }
        )
# Update the cheapest flight information to Google sheet
DataManager.UpdateCheaptestFlight(update_data)


