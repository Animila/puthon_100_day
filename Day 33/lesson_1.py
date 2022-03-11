import requests
# <Response [200]> - код ответа
# 1XX - подождать, пока что-то происходит
# 2XX - успешное выполнение
# 3XX - нет разрешения
# 4XX - ошибка
# 5XX - ошибка на сервере
data = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(data.status_code)
# if data.status_code == 404:
#     # исключение общего типа
#     raise Exception("Ресурс не был найден")
# elif data.status_code == 401:
#     raise Exception("Не достаточно прав доступа")
# обработка ошибок
data.raise_for_status()
# вывод данных
file = data.json()
# выбор ключа
longitude = file["iss_position"]["longitude"]
latitude = file["iss_position"]["latitude"]

print(file)
iss_position = (longitude, latitude)
print(iss_position)
