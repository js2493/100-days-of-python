import requests
import os
import datetime as dt

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 177.5
AGE = 22

app_id = os.getenv("nutritionix_id")
app_key = os.getenv("nutritionix_key")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheety_exercise_endpoint")


exercises = input("What exercises did you do today?: ")

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

parameters = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

current = dt.datetime.now()
date = current.strftime("%d/%m/%Y")
time = current.strftime("%X")

auth = ("username", "password")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=auth)
    # print(sheet_response.text)