# Flight Search

This class is to search for flight informaton, including the city code and flight ticket.

```py
import requests

tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_api = "yMehLUMCrfKBZ5wANlk1tYZVh70fBFXG"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    @classmethod
    def SearchCityCode(cls, city_name):
        query_endpoint = f'{tequila_endpoint}/locations/query'
        headers = {'apikey': tequila_api}
        query = {
            'term': city_name,
            "location_types": "city"
        }
        query_response = requests.get(url=query_endpoint, headers=headers, params=query)
        query_data = query_response.json()
        city_code = query_data['locations'][0]['code']
        return city_code

    @classmethod
    def SearchFlight(cls, from_city, to_city, date_from, date_to):
        pass

```


