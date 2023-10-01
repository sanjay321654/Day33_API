import requests
from datetime import datetime
LAT = 8.0844
LONG = 77.5495

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

now = datetime.now()
print(now.hour)
