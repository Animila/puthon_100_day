# try:
#     file = open("a_ile.txt")
#     dictional = {"key": 4}
#     print(dictional["k"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Wnek")
#     print("Файл не найден")
# except KeyError as error_text:
#     print(f"Ключ {error_text} не был найден")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Ошибка")
# # # собственные исключения
# # raise

height = float(input("Высота: "))
weight = int(input("Ширина: "))

if height > 3:
    # ошибка аргумента
    raise ValueError("Человек не может быть больше 3 метров")

bmi = weight / height ** 2
print(bmi)