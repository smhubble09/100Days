import requests
from flight_data import FlightData
from notification_manager import NotificationManager

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "2Y6ICO6SfEwK5Ivp1y619tGr6a8gssNy"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_dest_codes(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        location_headers = {"apikey": TEQUILA_API_KEY}
        location_params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=location_headers, params=location_params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "selected_cabins": "M",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
            "limit": 5,
        }
        flight_headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",params=flight_params,headers=flight_headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            leave_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.dest_city}: ${flight_data.price}")
        return flight_data
