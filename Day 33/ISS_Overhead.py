import time
import requests
import smtplib
from datetime import datetime

MY_LAT = 62.04372
MY_LONG = 129.73635

my_email = "19itypas70@gmail.com"
email_test = "hristoforovila5@gmail.com"
password = "Tomas_Kirit_Robert"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    'formatted': 0
}


def ISS_connect():
    print("Подключение к МКС...")
    data = requests.get(url="http://api.open-notify.org/iss-now.json")
    data.raise_for_status()
    file = data.json()

    longitude = float(file["iss_position"]["longitude"])
    latitude = float(file["iss_position"]["latitude"])
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True
    else:
        print('МКС не в вашей зоне...')


def SUN_connect():
    print("Подключение к погоде...")
    data = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data.raise_for_status()
    data_1 = data.json()

    sun = data_1["results"]["sunrise"].split("T")[1].split(':')[0]
    moon = data_1["results"]["sunset"].split("T")[1].split(':')[0]
    time_now = datetime.now()

    if time_now >= sun or time_now <= moon:
        return True
    else:
        print('Время неподходящее')

while True:
    if ISS_connect() and SUN_connect():
        print("отправка письма...")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_test,
                msg=f"Subject:ISS\n\nWEAK UP")

    print("ожидание...")
    time.sleep(6)
    print('прошло 6 секунд...')
