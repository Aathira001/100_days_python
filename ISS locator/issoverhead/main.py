import requests
from datetime import datetime
import smtplib
import time

LAT = 0.0000
LONG = 0.0000
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LAT - 5 <= iss_latitude <= LAT + 5 and LONG - 5 <= iss_longitude <= LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": LAT,
        "lng": LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject: ISS OVER YOU!\n\n The ISS is above you right now!"
        )
