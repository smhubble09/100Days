import requests
import os

USERNAME = os.environ.get("USERNAME")
PROJECT_NAME = "flightDeals"
SHEET_NAME = "users"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
BEARER = os.environ.get("BEARER")

sheety_headers = {
    "Authorization": F"Bearer {BEARER}",
}

print("Welcome to Shane's Flight Club.")
print("We find the best flight deals and email them to you.")
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email_diff = True
while email_diff:
    email = input("What's your email?\n")
    confirm_email = input("Confirm your email.\n")
    if email == confirm_email:
        email_diff = False


new_user = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}
response = requests.put(url=SHEETY_ENDPOINT, json=new_user, headers=sheety_headers)
print(response.text)