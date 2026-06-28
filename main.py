import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
api_key = os.environ["WEATHER_API_KEY"]





lat=36.830146
lon=-84.848640

parameters={
    "lat":lat,
    "lon":lon,
    "appid":api_key,
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
data_list=data["list"]
will_rain=False

for time_stamp in data_list:
    id=time_stamp["weather"][0]["id"]
    if id<700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="You probably will need an Umbrella☔",
        from_='whatsapp:+14155238886',
        to='whatsapp:+201113337224'
    )
    print(message.status)



