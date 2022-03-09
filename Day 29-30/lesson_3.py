fruits = ["Apple", "Pear", "Oracle"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("fruit pie")
    else:
        print(fruit + "pie")

make_pie(4)
# try:
#     make_pie(4)
# except IndexError:
#     print(f"Ошибка ключа")