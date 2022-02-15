from art import logo, vs
from game_data import data
import random

score = 0

# обработка запроса - сравнивание значений у двух значений

# вывод в консоль результата

def Generated_Word():
    count_list = len(data)
    currect_word = random.randint(0, count_list)
    word = data[currect_word]
    return word

def WinPlayer(variant_1, variant_2, choose):
    global score
    win = ''
    if variant_1['follower_count'] > variant_2['follower_count']:
        win = 'a'
    else:
        win = 'b'

    if choose == win:
        score += 1
        return True
    else:
        return False



def Game():
    exit = False
    while not exit:
        var_1 = Generated_Word()
        var_2 = Generated_Word()

        print(logo)
        print(f'Вариант А: {var_1["name"]} является {var_1["description"]} из {var_1["country"]}')
        print(vs)
        print(f'Вариант А: {var_2["name"]} является {var_2["description"]} из {var_2["country"]}')

        user = input('A или Б: ').lower()
        if WinPlayer(var_1, var_2, user):
            print(f'Вы угадали. Текущее количество очков {score}')
        else:
            print(f'Вы проиграли. Текущее количество очков {score}')
            exit = True



Game()
