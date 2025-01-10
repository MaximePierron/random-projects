from dotenv import load_dotenv
import os
import requests
from datetime import date, timedelta

load_dotenv()
tequila_api_key = os.environ["TEQUILA_API_KEY"]
tequila_endpoint = os.environ["TEQUILA_ENDPOINT"]
departure = os.environ["IATA_CODE_DEPARTURE"]

headers = {
    "apikey": tequila_api_key
}


def get_iata_code(city):
    query_endpoint = f"{tequila_endpoint}/locations/query"
    parameters = {
        "term": city,
        "location_types": "city"
    }
    response = requests.get(url=query_endpoint, params=parameters, headers=headers)
    data = response.json()
    city_info = data["locations"][0]
    code = city_info['code']
    return code


def search_for_flights(city_code):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    six_months = tomorrow + timedelta(days=6 * 30)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    six_months = six_months.strftime("%d/%m/%Y")

    parameters = {
        "fly_from": departure,
        "fly_to": city_code,
        "dateFrom": tomorrow,
        "dateTo": six_months,
        "nights_in_dst_from": 4,
        "nights_in_dst_to": 15,
        "max_stopovers": 1
    }

    search_endpoint = f"{tequila_endpoint}/v2/search"
    response = requests.get(url=search_endpoint, params=parameters, headers=headers)
    data = response.json()
    return data["data"]
