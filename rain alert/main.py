import requests
import smtplib
import os

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.environ.get("WEATHER_API_KEY")
EMAIL = "YOUR EMAIL"
PASSWORD = os.environ.get("EMAIL_PASSWORD")

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "app_id": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg="Subject: RAIN ALERT!\n\n It's going to rain! Don't forget to carry an umbrella!"
    )
