import requests
import datetime as dt
import smtplib
import time

email = "email"
password = "password"

# from latlong.net
MY_LAT = 34.052235
MY_LONG = -118.243683


def iss_overhead(latitude=MY_LAT, longitude=MY_LONG):
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(iss_response.raise_for_status())

    iss_data = iss_response.json()

    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    if abs(latitude - iss_latitude < 5) and abs(longitude - iss_longitude < 5):
        return True
    else:
        return False


def sun_down(latitude=MY_LAT, longitude=MY_LONG):
    parameters = {
        "lat": latitude,
        "long": longitude,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    results = data["results"]
    sunrise = results["sunrise"].split("T")[1].split(":")[:2]
    sunset = results["sunset"].split("T")[1].split(":")[:2]
    now = str(dt.datetime.now()).split(" ")[1].split(".")[0].split(":")[:2]
    for i in range(2):
        sunrise[i] = int(sunrise[i])
        sunset[i] = int(sunset[i])
        now[i] = int(now[i])
    if now[0] < sunrise[0] or now[0] > sunset[0]:
        return True
    elif (now[0] == sunrise[0] and now[1] < sunrise[1]) or (now[0] == sunset[0] and now[1] > sunset[1]):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if iss_overhead() and sun_down():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:Look Up\n\nThe ISS is currently above you!")
