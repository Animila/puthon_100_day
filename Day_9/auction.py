import os
from art import logo

bids = {}
stop_auction = False


def find_highest_bids(biding_record):
    highest_bids = 0
    winner = ''
    for i in biding_record:
        max = biding_record[i]
        if highest_bids < max:
            highest_bids = max
            winner = i
    print(f'Победитель {winner} с предложением в ${highest_bids}')


print(logo)
print("Добро пожаловать на закрытый аукцион")

while not stop_auction:
    name = input("Введите свое имя: ")
    price = int(input("Введите свое предложение: $"))
    bids[name] = price

    exit = input("Добавить новые ставки? (yes или no)\n")
    if exit == "yes":
        stop_auction = False
        os.system('CLS')
    else:
        stop_auction = True
        os.system('CLS')
        print("ИТОГИ")
        find_highest_bids(bids)
