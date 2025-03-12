import requests
import datetime


NUTRITIONIX_APPLICATION_ID = "808d7bxb8xxxx"
NUTRITIONIX_API_KEY = "271327edaa49759069c88500b430bccbxxx"
SHEETY_TOKEN = "dwfawfwaf"
GENDER = "male"
WEIGHT_KG = "55"
HEIGHT_CM = "165"
AGE = "21"


exercise_text = input("Tell me which exercises you did: ")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://"


requests_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

requests_headers = {
    "x-app-id": NUTRITIONIX_APPLICATION_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}


response = requests.post(url=exercise_endpoint, headers=requests_headers, json=requests_params)
info = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in info["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"{SHEETY_TOKEN}"
    }

    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
