import requests
import twilio.rest import Client


####################### Rain Check #####################################
OWM_ENDPOINT = "api.openweathermap.org/data/2.5/forecast"
API_KEY = 00000000000000000000
ACCOUNT_SID = '00000000000000000000'
AUTH_TOKEN = 00000000000000000000


parameters = {
    "lat" : 19.974545,
    "lon" : 73.833017,
    "cnt" : 4,
    "appid": API_KEY
}


response = requests.get(OWM_ENDPOINT, params=parameters)

response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella."
        from="000000000000000"
        to="0000000000000"
    )
    print(message.status)
