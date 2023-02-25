import requests
import datetime
import os
from twilio.rest import Client
import copy

NUM_HOURS = 24  # number of hours in future to look at

from_number = os.getenv("TWI_FROM_NUM") # Twilio number to send SMS from
to_number = os.getenv("TWI_TO_NUM") # Phone number to receive SMS - must be verified with Twilio
api_key = os.getenv("OWM_KEY")  # OpenWeather API key with OneCall
account_sid = os.getenv("TWI_SID") # Twilio account SID
auth_token = os.getenv("TWI_TOKEN")  # Twilio authorization token

# Los Angeles
MY_LAT = 34.02648590051866
MY_LONG = -118.34136307239534

current_hour = datetime.datetime.now().hour

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}

response = requests.get(url=OWM_endpoint, params=parameters)
weather_data = response.json()["hourly"]

low_temp: float
high_temp: float
rain_hours = []
clouds = [0, 0]

for i in range(NUM_HOURS):
    weather_id = int(weather_data[i]["weather"][0]["id"])
    temp = float(weather_data[i]["temp"])
    if i == 0:
        low_temp = float(weather_data[0]["temp"])

        high_temp = float(weather_data[0]["temp"])
    else:
        if low_temp > temp:
            low_temp = temp
        elif high_temp < temp:
            high_temp = temp
    if weather_id < 600:
        rain_hours.append(i)
    elif weather_id == 800:
        clouds[1] += 1
    elif weather_id > 800:
        clouds[0] += 1

low_temp = (low_temp - 273.15) * 9 / 5 + 32
high_temp = (high_temp - 273.15) * 9 / 5 + 32
low_temp = int(low_temp)
high_temp = int(high_temp)

rain_start = rain_hours[0]
rain_periods = []

rain_msg: str
if len(rain_hours) > 0:
    rain_start = rain_hours[0]
    rain_end = rain_hours[len(rain_hours) - 1]
    if len(rain_hours) < NUM_HOURS:
        for i in range(len(rain_hours) - 1):
            if rain_hours[i] + 1 != rain_hours[i + 1]:
                rain_periods.append([rain_start, rain_hours[i]])
                rain_start = rain_hours[i + 1]
        rain_periods.append([rain_start, rain_hours[len(rain_hours) - 1]])
        # if rain_hours[len(rain_hours)-1] - 1 != rain_hours[len(rain_hours)-2]:
        #     if rain_hours[len(rain_hours)-1]
print(rain_periods)
periods_AMPM = copy.deepcopy(rain_periods)
for i in range(len(rain_periods)):
    if (periods_AMPM[i][0] + current_hour) % 24 < 12:
        periods_AMPM[i][0] = " AM"
    else:
        periods_AMPM[i][0] = " PM"
    if (periods_AMPM[i][1] + current_hour) % 24 < 12:
        periods_AMPM[i][1] = " AM"
    else:
        periods_AMPM[i][1] = " PM"
    rain_periods[i] = [(str((x + current_hour) % 12) if (x + current_hour) % 12 != 0 else "12") for x in
                       rain_periods[i]]

if len(rain_periods) == 0:
    rain_msg = "It's going to rain the whole day!"
else:
    if len(rain_periods) == 1:
        rain_msg = f"It's going to rain today! 🌧️ from {rain_periods[0][0] + periods_AMPM[0][0]} to {rain_periods[0][1] + periods_AMPM[0][1]}."
    elif len(rain_periods) == 2:
        rain_msg = f"It's going to rain today! 🌧️ from {rain_periods[0][0] + periods_AMPM[0][0]} to {rain_periods[0][1] + periods_AMPM[0][1]} " \
                   f"and {rain_periods[1][0] + periods_AMPM[1][0]} to {rain_periods[1][1] + periods_AMPM[1][1]}."
    else:
        rain_msg = ""
        for i in range(len(rain_periods) - 1):
            rain_msg += " " + str(rain_periods[i][0]) + periods_AMPM[i][0] + " to " + str(rain_periods[i][1]) + \
                        periods_AMPM[i][1] + ","
        rain_msg += " and " + str(rain_periods[len(rain_periods) - 1][0]) + periods_AMPM[len(rain_periods) - 1][
            0] + " to " + str(
            rain_periods[len(rain_periods) - 1][1]) + periods_AMPM[len(rain_periods) - 1][1] + "."
        rain_msg = "It's going to rain today! 🌧️ from" + rain_msg

print(rain_hours)

weather_msg: str
if len(rain_hours) > 0:
    weather_msg = "-\n️" + rain_msg
else:
    weather_msg = "No rain today! It's going to be mostly " + "cloudy ☁️" if clouds[0] >= clouds[1] else "clear ☀️"
message = f"\n\nThe low today is {low_temp} and the high is {high_temp}."
message = weather_msg + message
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=message,
    from_=from_number,
    to=to_number
)