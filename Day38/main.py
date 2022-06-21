import requests
from datetime import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
USERNAME = os.environ.get("USERNAME")
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"
BEARER = os.environ.get("BEARER")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

excercise_post = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_params = {
    "query": input("Tell me what excercises you did: "),
    "gender": "male",
    "weight_kg": 82,
    "height_cm": 185,
    "age": 27,
}

response = requests.post(url=excercise_post, json=excercise_params,headers=headers)
excercise_json = response.json()["exercises"]


sheety_api = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
sheety_headers = {
    "Authorization": F"Bearer {BEARER}",
}

for exercise in excercise_json:
    now = dt.now()
    exercise_name = exercise["name"].title()
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]
    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%H:%M:%S")
    post_dict = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }
    post_result = requests.post(url=sheety_api,json=post_dict,headers=sheety_headers)
    print(post_result.text)