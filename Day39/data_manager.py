import requests
import os

USERNAME = os.environ.get("USERNAME")
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

BEARER = os.environ.get("BEARER")
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.dest_data = {}

    def get_dest_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
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
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
