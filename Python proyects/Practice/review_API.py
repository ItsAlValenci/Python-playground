import json
import requests

# response = requests.get(url= "http://api.open-notify.org/iss-now.json")

# data = response.json()

# longitud = data["iss_position"]['latitude']
# latitud = data["iss_position"]['longitude']

# location = (longitud,latitud)


# print(location)

MY_LATITUD = 37.790782
MY_LONGITUD = -122.406325


parameters = {
    "lat": MY_LATITUD,
    "lng": MY_LONGITUD,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)