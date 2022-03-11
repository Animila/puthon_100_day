import requests
from datetime import datetime

MY_LAT = 40.785091
MY_LONG = -73.968285

# создание запроса в API
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    'formatted': 0
}

# получение данный API c использованием данных
data = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# обработка исключений
data.raise_for_status()
# преобразование в JSON
data_1 = data.json()
# выводим результат работы
sun = data_1["results"]["sunrise"]
moon = data_1["results"]["sunset"]

# обрезка
sun_time = sun.split("T")[1].split(':')[0]
moon_time = moon.split("T")[1].split(':')[0]
print(sun_time)
print(moon_time)

time_now = datetime.now()
print(time_now.hour)
