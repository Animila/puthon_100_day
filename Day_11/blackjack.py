import os
from art import logo
import random


# Правила
# Размер колоды не ограничен.
# Шутников не бывает.
# Валет/Дама/Король считаются за 10.
# Туз может считаться 11 или 1.
# Карты в списке имеют равную вероятность быть разыгранными.
# Карты не удаляются из колоды по мере их вытягивания.
# Компьютер - это дилер.

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return sum(list)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return 'Ничья'
    elif comp_score == 0:
        return 'Проигрыш, у аппонента Блэкджек'
    elif user_score == 0:
        return 'Победа, у вас Блэкджек'
    elif user_score > 21:
        return 'У вас слишком много - вы проиграли'
    elif comp_score > 21:
        return 'У компьютера слишком много - вы выйграли'
    elif user_score > comp_score:
        return 'Вы выйграли'
    else:
        return 'Вы проиграли'


def Game():
    print(logo)

    exit = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not exit:
        user = calculate_score(user_cards)
        comp = calculate_score(computer_cards)

        print(f"Ваши карты: {user_cards}, текущий счет: {user}")
        print(f'Первая карта компьютера: {computer_cards[0]}')

        if user == 0 or comp == 0 or user > 21:
            exit = True
        else:
            exing = input("Добавить еще карту?\n").lower()
            if exing == "yes" or exing == "да":
                user_cards.append(deal_card())
            else:
                exit = True

    while comp != 0 and comp < 17:
        computer_cards.append(deal_card())
        comp = calculate_score(computer_cards)

    print(f'Твоя финальная колода: {user_cards}, финальный счет: {user}')
    print(f'Финальная колода компьютера: {computer_cards}, финальный счет: {comp}')
    print(compare(user, comp))


while input('Хотите ли вы сыграть еще раз? "y" или "n": ') == 'y':
    os.system('CLS')
    Game()
