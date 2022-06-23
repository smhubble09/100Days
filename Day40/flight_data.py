class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, depart_city, depart_airport, destination_city, destination_airport, out_date, return_date,stop_overs=0,via_city="") -> None:
        self.price = price
        self.depart_city = depart_city
        self.depart_airport = depart_airport
        self.dest_city = destination_city
        self.dest_airport = destination_airport
        self.leave_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city