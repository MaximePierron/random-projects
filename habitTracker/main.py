import os
import requests
from dotenv import load_dotenv
from datetime import date
from datetime import timedelta

load_dotenv()
auth_token = os.getenv("PIXELA_AUTH_TOKEN")
username = os.getenv("PIXELA_USERNAME")


user_parameters = {
    "token": auth_token,
    "username": username,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

pixela_create_user_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_parameters)

graph_parameters = {
    "id": "readinghabits1",
    "name": "My reading habits of 2023",
    "unit": "page",
    "type": "int",
    "color": "momiji",
    "timezone": "Europe/Berlin",
}

headers = {
    "X-USER-TOKEN": auth_token
}

pixela_create_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
# response = requests.post(url=pixela_create_graph_endpoint, json=graph_parameters, headers=headers)

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

pixel_parameters = {
    "date": day_before_yesterday.strftime("%Y%m%d"),
    "quantity": "14",
}

pixela_reading_id = "readinghabits1"
pixela_post_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{pixela_reading_id}"
response = requests.post(url=pixela_post_pixel_endpoint, json=pixel_parameters, headers=headers)

print(response.text)



