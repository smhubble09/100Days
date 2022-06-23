#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "SLC"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_dest_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_dest_codes(city_names)
    data_manager.update_dest_codes(codes)
    sheet_data = data_manager.get_dest_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(weeks= 26)

for destination in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

    if flight.price < destination["lowestPrice"]:
            notification_manager.send_text(
                message= f"Low price alert! Only ${flight.price} to fly from {flight.depart_city}-{flight.depart_airport} to {flight.dest_city}-{flight.dest_airport}, from {flight.leave_date} to {flight.return_date}."
            )
