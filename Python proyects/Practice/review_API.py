import json
import requests

response = requests.get(url= "http://api.open-notify.org/iss-now.json")

data = response.json()

longitud = data["iss_position"]['latitude']
latitud = data["iss_position"]['longitude']

location = (longitud,latitud)


print(location)
