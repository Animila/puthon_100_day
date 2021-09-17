import random

# Задаем параметр, который будет использоваться для генерации случайного числа
test_seed = int(input('Номер для генерации: '))
random.seed(test_seed)

# Генерируем случайное число
random_size = random.randint(0,1)

# Проверяем
if random_size == 1:
    print("Орел")
else:
    print("Решка")