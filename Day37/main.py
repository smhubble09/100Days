import requests
from datetime import datetime as dt

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#Create new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Create new graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Reading Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji",
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Create new pixel
today = dt.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes were read today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

#Update pixel
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220615"

# pixel_update_data = {
#     "quantity": "78",
# }

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

#Delete pixel
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220615"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)