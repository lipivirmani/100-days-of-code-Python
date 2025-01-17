import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = "68"
HEIGHT_CM = "158"
AGE = "22"

APP_ID = os.environ["76ee0e8c"]
API_KEY = os.environ["990d93f51b169dbc0698b89502307fb0"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["https://api.sheety.co/6dfae5405d240230d9f958c2a45ab3d8/workoutTracking/workouts"]

exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers_sheety = {"Authorization": "bGlwaTpMaXBpdmlybWFuaQ", }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=headers_sheety)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "lipi", "Password"
        )
    )
    print(sheet_response.text)
