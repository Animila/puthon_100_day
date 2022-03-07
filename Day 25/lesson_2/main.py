import pandas

# data = pandas.read_csv("../lesson_1/weather-data.csv")
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)

# # получение из столбца строки в виде массива
# temp = data["temp"].to_list()
# print(temp)

# #средняя темепаратура
# avarage = sum(temp) / len(temp)
# print(avarage)
# # альтернатива
# print(data['temp'].mean())

# # максимальная температура
# print(data['temp'].max())

# # получить столбец
# print(data['condition'])
# print()
# print(data.condition)
# print()

# # Получить данные в строке
# print(data[data.day == 'Monday'])
# print()
# print(data[data.temp == data.temp.max()])

# # проверяем соответствие на "понедельник"
# monday = data[data.day == 'Monday']
# # # выводим погоду и погоду в понедельник
# # print(monday.condition)
# # print()
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# создание соей таблицы
data_dict = {
    'students': ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")