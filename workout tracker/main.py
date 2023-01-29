import requests
from datetime import datetime

GENDER = "GENDER"
WEIGHT_KG = "WEIGHT"
HEIGHT_CM = "HEIGHT"
AGE = "AGE"

APP_ID = "YOUR ID"
APP_KEY = "YOUR KEY"

SHEET_UNAME = "YOUR UNAME"
SHEET_PASSWORD = "YOUR PASSWORD"

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "YOUR URL"

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
