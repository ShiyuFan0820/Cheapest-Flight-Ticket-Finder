import requests

sheety_endpoint = "https://api.sheety.co/596407487435113fa1b524e86a87b95d/flightDeal/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    ## Define a method to get the city names from the Google Sheet.
    @classmethod
    def GetCityInfo(cls):
        '''

        :return: City information on the Google Sheet.
        '''
        response = requests.get(sheety_endpoint)
        city_info = response.json()['prices']
        return city_info

    @classmethod
    def UpdateCityCode(cls, cities_info):
        '''

        :param cities_info: A list of dictionary, each dictionary inludes the updated information of the cities.
        :return: None
        '''
        for row in cities_info:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{row['id']}",
                json=new_data
            )
            print(f"{row["city"]}'s IATA Code has been updated successfully.")
        return

