import requests

tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_api_key = "yMehLUMCrfKBZ5wANlk1tYZVh70fBFXG"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    @classmethod
    def SearchCityCode(cls, city_name):
        '''

        :param city_name: Name of the city.
        :return: The city code.
        '''
        query_endpoint = f'{tequila_endpoint}/locations/query'
        headers = {'apikey': tequila_api_key}
        query = {
            'term': city_name,
            "location_types": "city"
        }
        query_response = requests.get(url=query_endpoint, headers=headers, params=query)
        query_data = query_response.json()
        city_code = query_data['locations'][0]['code']
        return city_code

    @classmethod
    def SearchFlight(cls, fly_from, fly_to, date_from, date_to, adults=1, children=0, infants=0, selected_cabins="M", curr="GBP", max_stopovers=0, one_for_city=0, ret_from_diff_city=False, ret_to_diff_city=False):
        search_endpoint = f"{tequila_endpoint}/v2/search"
        headers = {
            "apikey": tequila_api_key
        }
        info = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "adults": adults,
            "children": children,
            "infants": infants,
            "selected_cabins": selected_cabins,
            "curr": curr,
            "max_stopovers": max_stopovers,
            "one_for_city": one_for_city,
            "ret_from_diff_city": ret_from_diff_city,
            "ret_to_diff_city": ret_to_diff_city
        }
        response = requests.get(
            url=search_endpoint,
            headers=headers,
            params=info
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found from {fly_from} to {fly_to}.")
            return None
        return response.json()["data"]

