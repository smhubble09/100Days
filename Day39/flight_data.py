class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date) -> None:
        self.price = price
        self.depart_city = origin_city
        self.depart_airport = origin_airport
        self.dest_city = destination_city
        self.dest_airport = destination_airport
        self.leave_date = out_date
        self.return_date = return_date