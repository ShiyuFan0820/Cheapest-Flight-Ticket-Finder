import requests

# Replace it with your own endpoint.
sheety_endpoint = "https://api.sheety.co/596407487435113fa1b524e86a87b95d/flightDeal/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    ## Define a method to get the city names from the Google Sheet.
    @classmethod
    def GetCityInfo(cls):
        """

        :return: City information on the Google Sheet.
        """
        response = requests.get(sheety_endpoint)
        city_info = response.json()['prices']
        return city_info

    @classmethod
    def UpdateCityCode(cls, row_id, city_code):
        """

        :param row_id: City's row id.
        :param city_code: City's code
        :return: None
        """
        new_data = {
            "price": {
                "iataCode": city_code
            }
        }
        response = requests.put(
            url=f"{sheety_endpoint}/{row_id}",
            json=new_data
        )
        print("IATA Code has been updated successfully.")
        return

    @classmethod
    def UpdateCheaptestFlight(cls, update_data):
        """

        :param update_data: A list of dictionary, each dictionary inludes the updated information of the cities.
        :return: None
        """
        for row in update_data:
            new_data = {
                "price": {
                    "lowestPrice": row["cheapest_flight"]["price"],
                    "fromAirport": row["cheapest_flight"]["from_airport"],
                    "toAirport": row["cheapest_flight"]["to_airport"],
                    "departureDate": row["cheapest_flight"]["departure_date"],
                    "departureTime": row["cheapest_flight"]["departure_time"],
                    "arrivalDate": row["cheapest_flight"]["arrival_date"],
                    "arrivalTime": row["cheapest_flight"]["arrival_time"],
                    "orderLink": row["cheapest_flight"]["order_link"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{row['id']}",
                json=new_data
            )
            print(f"{row["city"]}'s flight information has been updated successfully.")
        return
