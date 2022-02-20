from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    '''Форматрирование строки под значения от словаря'''
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, {account_descr}, из {account_country}'

def check_answer(yser, wording_1, wording_2):
    '''Проверка ответа и количества подписчиков и возврат логического значения'''
    if wording_1 > wording_2:
        return user == 'a'
    else:
        return user == 'b'

print(logo)
score = 0
exit = False
account_b = random.choice(data)

while not exit:
    word_1 = account_b
    word_2 = random.choice(data)
    if word_1 == word_2:
        word_2 = random.choice(data)

    print(f'Вариант А: {format_data(word_1)}')
    print(vs)
    print(f'Вариант Б: {format_data(word_2)}')

    user = input('Выберите вариант: А или Б: ').lower()

    word_count_1 = word_1['follower_count']
    word_count_2 = word_2['follower_count']
    is_correct = check_answer(user, word_count_1, word_count_2)

    os.system('cls')

    if is_correct:
        score += 1
        print(f'Вы правы. Твой счет {score}')
    else:
        print(f'Увы, вы проиграли. Ваш счет {score}')
        exit = True