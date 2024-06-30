import requests
import os

TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
IATA_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY") 
        self._api_pass = os.environ.get("AMADEUS_API_PASS")
        self._token = self._get_new_token()
        
    def _get_new_token(self):
        # https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/API-Keys/authorization/
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        print(header)
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_pass
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=data, verify=False)
        response.raise_for_status()
        access_token = response.json()['access_token']
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        if not access_token:
            raise Exception('Failed to obtain access token')
        return access_token
        
    def search_iatacode(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        
        params = {
            'keyword': city_name,
            'max': 2,
            'include': 'AIRPORTS'
        }
        
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=params, verify=False)
        # print(response.json())
        
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        
        return code
    
    def check_flight(self, original, destination, departure_date, return_date, adults=1, currency='CAD', nonstop="true"):
        headers = {'Authorization': f"Bearer {self._token}",
                   }
        
        params = {
            'originLocationCode': original,
            'destinationLocationCode' : destination,
            'departureDate': departure_date,
            'returnDate': return_date,
            'adults': adults,
            'currencyCode': currency,
            'nonStop': nonstop,
            'max': 10,
        }
        
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=params, verify=False)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.")
            print("Response body:", response.text)
            return None
        
        return response.json()