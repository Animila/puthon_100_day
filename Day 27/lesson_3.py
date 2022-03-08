# def calculation(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs['multiply']
#     print(n)
#     # print(kwargs)
#     # print(type(kwargs))
#
#     # # перебор словаря
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#     # # вывод значения по ключу
#     # print(kwargs['add'])
#
# calculation(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        # чтобы не было ошибок
        self.name = kw.get("name")
        self.seats = kw.get("color")

my_car = Car(make="Nissan", model="GT-R", color="blue")
print(my_car.model)
print(my_car.make)
print(my_car.name)
print(my_car.seats)
