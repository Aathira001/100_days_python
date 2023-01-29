import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 63
HEIGHT_CM = 163
AGE = 25

APP_ID = "cdfdbb71"
APP_KEY = "efda0b188645b252c898050211baae12"

SHEET_UNAME = "aa"
SHEET_PASSWORD = "qwerty1234"

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "https://api.sheety.co/fb9aa5cc65943579ed0804defbdcb47f/copyOfMyWorkouts/workouts"

query = input("Please tell me what you did today: \t")

headers = {
    "x-app-id": APP_ID,
    "x-app-keY": APP_KEY,
}

params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_url, json=params, headers=headers)
response.raise_for_status()

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

    sheet_response = requests.post(sheet_url, json=sheet_inputs, auth=(SHEET_UNAME, SHEET_PASSWORD))

    print(sheet_response.text)
