class FlightData:
    def __init__(self, price, original, destination, departure_date, return_date, carrier_code):
        self.price = price
        self.original = original
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.carrier_code = carrier_code
        
def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData('N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
    
    #Find information about the 1st flight on the list
    first_flight = data['data'][0]
    lowest_price = first_flight['price']['grandTotal']
    departure = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    arrival = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    departure_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    return_date = first_flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]
    carrier_code = first_flight['itineraries'][0]['segments'][0]['carrierCode']
    
    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, departure, arrival, departure_date, return_date, carrier_code)
    
    for flight in data['data']:
        if flight['price']['grandTotal'] < lowest_price:
            lowest_price = flight['price']['grandTotal']
            departure = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            arrival = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            departure_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            return_date = flight['itineraries'][1]['segments'][0]['departure']['at'].split('T')[0]
            carrier_code = flight['itineraries'][0]['segments'][0]['carrierCode']
            
            cheapest_flight = FlightData(lowest_price, departure, arrival, departure_date, return_date, carrier_code)
            print(f"Lowest price to {arrival} is CAD{lowest_price}")
    
    return cheapest_flight