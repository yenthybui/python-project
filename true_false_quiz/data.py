import requests

parameters = {
    'amount': 20,
    'type': 'boolean',
    # 'category': 10
}

response = requests.get(url='https://opentdb.com/api.php', params = parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']