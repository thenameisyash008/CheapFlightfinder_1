from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d46c95f5c31ce41f54b8a1a5a7b690d2/copyOfFlightDeals/prices"

response = requests.get(SHEETY_PRICES_ENDPOINT)
result = response.json()

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

