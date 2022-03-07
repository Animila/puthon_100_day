# with open('weather-data.csv') as data_files:
#     data = data_files.readlines()
# #     print(data)

# import csv
# with open("weather-data.csv") as data_files:
#     data = csv.reader(data_files)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(row[1])
#
#     print(temp)

import pandas

data = pandas.read_csv("weather-data.csv")
print(data['temp'])
