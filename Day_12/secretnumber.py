import random

NUMBER = random.randint(0, 100)
count = 0
exit = False

print('Добро пожаловать в игру "угадай число"')
print("Я загадал число от 1 до 100")

level = input("Выбери сложность. Напиши (easy) или (hard): ")
if level == 'hard':
    count = 5
elif level == 'easy':
    count = 10

while not exit:
    if count == 0:
        print(f'Вы проиграли. Загаданное число {NUMBER}')
        exit = True
    else:
        print(f'У вас есть {count} попыток')

        user = int(input('Ваше число: '))
        if user > NUMBER:
            print('Слишком высоко')
            print('Повтори попытку')
            count -= 1
        elif user < NUMBER:
            print('Слишком низко')
            print('Повтори попытку')
            count -= 1
        else:
            print('Вы выйграли')
            exit = True
