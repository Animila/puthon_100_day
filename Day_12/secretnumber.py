import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_diffucult():
    level = input("Выбери сложность. Напиши (easy) или (hard): ")
    if level == 'hard':
        return HARD_LEVEL
    elif level == 'easy':
        return EASY_LEVEL


def check_answer(user, answer, count):
    '''проверка ответа на совпадение. возврат оставшихся шагов'''
    if user > answer:
        print('Слишком высоко')
        return count - 1
    elif user < answer:
        print('Слишком низко')
        return count - 1
    else:
        print('Вы выйграли')


def game():
    print('Добро пожаловать в игру "угадай число"')
    print("Я загадал число от 1 до 100")

    NUMBER = random.randint(0, 100)
    print(f'для разработки: {NUMBER}')

    count = set_diffucult()


    user = 0
    while user != NUMBER:
        print(f'У вас осталось {count} попыток')
        user = int(input('Ваше число: '))
        count = check_answer(user, NUMBER, count)
        if count == 0:
            print(f'Вы проиграли. Правильный ответ: {NUMBER}')
            return
        elif user != NUMBER:
            print('Повторите снова')




game()
