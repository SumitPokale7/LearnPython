# https://pixe.la/

import requests
import datetime

USERNAME = "masti"
TOKEN = "toosensitiveinfo"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

header = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Riding Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# yesterday_date = datetime.datetime(year=2025, month=3, day=10)
today = datetime.datetime.now()


post_graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "103.4",
}
response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=post_graph_config, headers=header)
print(response.text)
