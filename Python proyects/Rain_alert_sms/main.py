import os
import requests
from twilo.rest import Client
from twilio.http.http_client import TwilioHttpClient


#Setting to connect Twilio in automated pythonanywhere server
proxy_client = TwilioHttpClient
propxy_client.session.proxies = {
    "http": os.environ.get("HTTP_PROXY"),
}

## Variables to connect to openweathermap and twilio
api_key = "e4e7a57e97a569809b4ba8714bb6c600"
my_lat = 37.774929
my_long= -122.419418

# Openweather API parameters
weather_parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,
}
# Twilio parameters
account_sid = "AC70000000000000000000000000000000"
auth_token = "using_auth_token"

address = "https://api.openweathermap.org/data/2.5/forecast"

# Making the request to OpenWeatherMap API
response = requests.get(address,params=weather_parameters)
response.raise_for_status

weather_data = response.json()

# checking if it will rain today in set location 
will_rain_today = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    weather_type = hour_data["weather"][0]["main"]
    if weather_id < 700:
        will_rain_today = True

# we only print one message it will rain today at some point 
if will_rain_today:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella!",
        from_='+41500000000',
        to='+141555555555'
    )
    print(message.status)
