# # открыть файл
# file = open('my_files.txt')
# # записать в переменную все что есть в файле
# content = file.read()
# print(content)
# # обязательно закрыть
# file.close()

# # Как делают все:
# with open('my_files.txt') as file:
#     content = file.read()
#     print(content)

# Моды: r - чтение, w - перезапись (или создание файла), a - поверх записей
with open('new_files.txt', mode='w') as file:
    file.write('\nNew text.')
