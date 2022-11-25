import requests
from datetime import datetime

parameters = {
    "lat": 40.762972,
    "lng": 30.352318,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)

data=response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now=datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
