import requests

USERNAME = "d7857d475b7faf250d8f5d7ee6b66e8a"
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

BEARER = "l!6pmVC^mwPAT&aUmftvZ^4ojuN72p%Wuq6K^hgWGD0&yn0yEAoglBtEHe!z8my1AO0Q4"
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
