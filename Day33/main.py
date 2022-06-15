from time import sleep
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LNG = -0.127758 # Your longitude
MY_EMAIL = "test@email.com"
PASSWORD = "NotA Password#41"

#Your position is within +5 or -5 degrees of the ISS position.
def within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5) and (iss_longitude <= MY_LNG + 5 and iss_longitude >= MY_LNG - 5):
        return True

#Is it currently dark?
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
while within_range() and is_dark:
    # Then send me an email to tell me to look up.
    with smtplib.SMTP("smtp.test.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="test@email.com", 
                msg=f"Subject:ISS Above Now!\n\nLook up!")
    # BONUS: run the code every 60 seconds.
    sleep(60)
