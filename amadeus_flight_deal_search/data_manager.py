import requests
import os

sheety_auth = os.environ.get("SHEETY_AUTH_TOKEN")

url = 'https://api.sheety.co/ded0dd949823cd319936c51f2260eab6/flightDealFinder/prices'
headers = {
    'Authorization': sheety_auth,
}

class DataManager:
    
    def update_iatacode(self, id, code):
        body = {
            'price': {
                'iataCode': code,
            }
        }
    
        response = requests.put(url=f'{url}/{id}', headers=headers, json=body)
        
        if response.ok:
            print('Update successful!')
            print(response.json())
        else:
            print(f'Update failed with status code: {response.status_code}')
            print(response.text)