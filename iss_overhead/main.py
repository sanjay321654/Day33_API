import requests
from datetime import datetime
from smtplib import SMTP
import time

my_email = "pythoncourse20102002@gmail.com"
my_password = "tenq ovqz kxvu wghm"

MY_LAT = 8.0844
MY_LONG = 77.5495


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now < sunrise or time_now > sunset:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sanjay20102002@yahoo.com",
                            msg="Subject: Look Up\n\n The ISS is above you in the sky.")
