class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Я дышу")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('делаю это под водой')

    def swim(self):
        print("Я плаваю в воде")


nemo = Fish()
nemo.swim()
nemo.breathe()