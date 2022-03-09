# попытка запуска
try:
    file = open("a_ile.txt")
    dict = {"key": 4}
    print(dict["k"])
# если ошибка
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Wnek")
    print("Файл не найден")
except KeyError as error_text:
    print(f"Ключ {error_text} не был найден")
# если все получилось
else:
    content = file.read()
    print(content)
# срабатывает не важно от того, что произойдет
finally:
    file.close()
    print("Файл был закрыт")

