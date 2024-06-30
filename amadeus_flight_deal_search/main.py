import requests
import time
import datetime
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight
import os

ORIGIN_CITY_IATA = "YYZ"
flight_search = FlightSearch()
data_manager = DataManager()

# Extract information from GGSheet
sheety_auth = os.environ.get("SHEETY_AUTH_TOKEN")

url = 'https://api.sheety.co/ded0dd949823cd319936c51f2260eab6/flightDealFinder/prices'
headers = {
    'Authorization': sheety_auth,
}

response = requests.get(url, headers=headers)
sheet_data = response.json()['prices']

# Fill iatacode if not existed
for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.search_iatacode(row['city'])
        data_manager.update_iatacode(row['id'], row['iataCode'])
        # slowing down requests to avoid rate limit
        time.sleep(2)
 
# Define datetime range for flight search
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
six_months_from_now = today + datetime.timedelta(days=6*30)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flight(ORIGIN_CITY_IATA, destination['iataCode'], tomorrow, six_months_from_now)
    # flights = flight_search.check_flight(ORIGIN_CITY_IATA, destination['iataCode'], '2024-07-29', '2024-08-03')
    
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: CAD{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    
    if cheapest_flight.price == 'N/A':
        print('Price is not available')
    elif float(cheapest_flight.price) <= destination['lowestPrice']:
        notification_manager = NotificationManager(cheapest_flight.price, cheapest_flight.original, cheapest_flight.destination, 
                     cheapest_flight.departure_date, cheapest_flight.return_date, cheapest_flight.carrier_code)
        notification_manager.send_message()
    else:
        print('Price is not lower than set threshold.')