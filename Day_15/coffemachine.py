MENU = {
    "espresso":
        {
            "ingredients":
                {
                    "water": 50,
                    "coffee": 18,
                },
            "cost": 1.5,
        },
    "latte":
        {
            "ingredients":
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            "cost": 2.5,
        },
    "cappuccino":
        {
            "ingredients":
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            "cost": 3.0,
        }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource(order_ingredient):
    '''Возвращает True или False если не хватает ресурсов'''
    no_need = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print('Простите, но нет воды')
            no_need = False
    return no_need


def process_coins():
    '''Возврат общей суммы монет'''
    print('Введите моенты')
    total = int(input('Сколько четвертаков?: ')) * 0.25
    total += int(input('Сколько цент?: ')) * 0.1
    total += int(input('Сколько пятаков?: ')) * 0.05
    total += int(input('Сколько пенни?: ')) * 0.01
    return total


def successful(money_received, drink_cost):
    '''Возвращает True когда платеж принят, или False если не прошло внимания'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Получите ${change} сдачи")
        global profit
        profit += drink_cost
        return True
    else:
        print("Прошу прощения, платеж не принят, денег мало")
        return False

def make_coffee(drink_name, order_ingredient):
    '''Вычитает необходимые ингредиенты'''
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'Получите свой {drink_name}')


profit = 0
exit = False

while not exit:
    choose = input('Что бы вы хотели? (espresso/latte/cappuccino): ')
    if choose == 'off':
        exit = True
    elif choose == 'report':
        print(f'Вода: {resources["water"]}ml')
        print(f'Молоко: {resources["milk"]}ml')
        print(f'Кофе: {resources["coffee"]}ml')
        print(f'Монеты: ${profit}')
    else:
        drink = MENU[choose]
        if resource(drink["ingredients"]):
            payment = process_coins()
            if successful(payment, drink['cost']):
                make_coffee(choose, drink['ingredients'])
