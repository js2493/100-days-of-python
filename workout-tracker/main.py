import requests
import os

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 177.5
AGE = 22.5

app_id = os.getenv("nutritionix_id")
app_key = os.getenv("nutritionix_key")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)
