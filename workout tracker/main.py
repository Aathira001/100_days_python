import requests

GENDER = "female"
WEIGHT_KG = 63
HEIGHT_CM = 163
AGE = 25

APP_ID = "cdfdbb71"
APP_KEY = "efda0b188645b252c898050211baae12"

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

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

response = requests.post(url=exercise_url, headers=headers, json=params)
response.raise_for_status()

result = response.json()
print(result)
