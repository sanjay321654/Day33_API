import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
print(longitude)

