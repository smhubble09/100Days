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
    data_manager.city_codes = flight_search.get_dest_codes(city_names)
    data_manager.update_dest_codes()
    sheet_data = data_manager.get_dest_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(weeks= 26)

for destination_code in destinations:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_months
    )

    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message= f"Low price alert! Only ${flight.price} to fly from {flight.depart_city}-{flight.depart_airport} to {flight.dest_city}-{flight.dest_airport}, from {flight.leave_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.depart_airport}.{flight.dest_airport}.{flight.leave_date}*{flight.dest_airport}.{flight.depart_airport}.{flight.return_date}"
        
        notification_manager.send_emails(emails, message, link)