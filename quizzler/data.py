import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()["results"]