import requests
from datetime import datetime as dt



parameters = {
    "lat": 39.933365,
    "lon": 32.859741,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)

# response.raise_for_status()

data = response.json()
codes = []


def check_rain12hours(p_data):
    weather_data = p_data["hourly"]
    mesg = ""
    for weather_dict in weather_data:
        weather = weather_dict["weather"][0]
        weather_time = dt.fromtimestamp(weather_dict["dt"])
        codes.append(weather["id"])
        if weather["id"] < 700:
            mesg = mesg + f"It will {weather['main'].lower()} at {weather_time} ❤️\n"

    return mesg


msg = check_rain12hours(data)
if msg == "":
    msg = "No rainy weather in 12 hours ❤️"
print(msg)

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = ACC_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=msg,
  from_=FROM,
  to=YOUR_NUMBER
)

print(message.sid)