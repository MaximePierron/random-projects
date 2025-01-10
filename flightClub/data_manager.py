from dotenv import load_dotenv
import os
import requests

load_dotenv()
sheety_endpoint_prices = os.environ["SHEETY_ENDPOINT_PRICES"]
sheety_endpoint_users = os.environ["SHEETY_ENDPOINT_USERS"]
sheety_api_token = os.environ["SHEETY_AUTH_TOKEN"]
sheety_headers = {
    "Authorization": f"Bearer {sheety_api_token}",
    "Content-Type": "application/json"
}


def get_prices():
    response = requests.get(url=sheety_endpoint_prices, headers=sheety_headers)
    data = response.json()
    sheet_data = data['prices']
    return sheet_data


def put_iata_code(city_id, iata_code):
    parameters = {
        "price": {
            "iataCode": iata_code
        }
    }
    response = requests.put(url=f"{sheety_endpoint_prices}/{city_id}", json=parameters, headers=sheety_headers)
    print(response.text)


def get_users():
    response = requests.get(url=sheety_endpoint_users, headers=sheety_headers)
    data = response.json()
    sheet_data = data['users']
    return sheet_data
