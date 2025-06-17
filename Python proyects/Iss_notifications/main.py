import requests
from datetime import datetime
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os
import random
import time

MY_LAT = 37.790782 # Your latitude
MY_LONG = -122.406325 # Your longitude

def is_iss_in_sky():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <=5:
        return True


def is_night(): 
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    time_now = datetime.now().hour

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now >= sunset or time_now <= sunrise:
        return True


def email_sender( ):
    load_dotenv()
    EMAIL_PASSWORD = os.getenv("EMAIL_KEY")

    MY_EMAIL = "my_email@gmail.com"
    message = "Space Time Baby"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls() #to make connection secure

        connection.login(user= MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs=MY_EMAIL, 
            msg= f"Subject: Look Up\n\n{message}"
        )


while True:
    time.sleep()
    if is_iss_in_sky() and is_night():
        email_sender()
    else:
        print("Nothing to see at the current moment!!\n\n")

