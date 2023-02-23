import datetime

import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.getenv("pixela_user")
TOKEN = os.getenv("pixela_token")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)
def add_data(hours, date=datetime.datetime.now().strftime("%Y%m%d")):
    pixel_data = {
        "date": date,
        "quantity": str(hours)
    }

    graph1_endpoint = graph_endpoint + "/graph1"
    response = requests.post(url=graph1_endpoint, json=pixel_data, headers=headers)
    print(response.text)


add_data(4, "20230222")
