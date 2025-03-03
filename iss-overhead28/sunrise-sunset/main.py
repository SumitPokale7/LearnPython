# https://api.sunrise-sunset.org/json

import requests
from datetime import datetime


LAT = 19.997454
LNG = 73.789803

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = datetime.now()


print(time_now.hour)