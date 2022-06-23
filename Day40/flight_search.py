import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_codes = []

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
        }
        flight_headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",params=flight_params,headers=flight_headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            flight_params["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=flight_headers,params=flight_params)
            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                depart_city=data["route"][0]["cityFrom"],
                depart_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                leave_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
