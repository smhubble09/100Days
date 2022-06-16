import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 35.939030,
    "lon": -77.800240,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("WEATHER_APPID"),
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]
hourly_weather_id = [item["weather"][0]["id"] for item in hourly_data]

bring_umbrella = False
for id in hourly_weather_id:
    if id < 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring and umbrella!",
            from_="NumberGoesHere",
            to="AnotherNumberGoesHere"
        )
    print(message.status)