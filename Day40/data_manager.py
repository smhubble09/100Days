import requests
import os

USERNAME = os.environ.get("USERNAME")
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{USERNAME}/flightDeals/prices"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{USERNAME}/flightDeals/users"
BEARER = os.environ.get("BEARER")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.dest_data = {}

    def get_dest_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.dest_data = data["prices"]
        return self.dest_data

    def update_dest_codes(self):
        for city in self.dest_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
