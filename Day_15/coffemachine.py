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

money = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,

}


def money_check():
    one = money['quarter'] * int(input('Сколько центов?: '))
    two = money['dime'] * int(input('Сколько динариев?: '))
    three = money['nickel'] * int(input('Сколько фунты?: '))
    four = money['penny'] * int(input('Сколько пенни?: '))
    sum = round(one + two + three + four, 2)
    return sum


def drink_give(user):
    drink_user = MENU[user]
    structure = drink_user['ingredients']
    if structure['water'] >= resources['water']:
        resources['water'] -= structure['water']

    if structure['coffee'] >= resources['coffee']:
        resources['coffee'] -= structure['coffee']

    if user != 'expresso':
        if structure['milk'] >= resources['milk']:
            resources['milk'] -= structure['milk']


def reporting():
    print(f'Вода: {resources["water"]}ml')
    print(f'Молоко: {resources["milk"]}ml')
    print(f'Кофе: {resources["coffee"]}ml')


def CoffeMachine():
    exit = False
    while not exit:
        user = input('Что бы вы хотели? (latte/expresso/cappuccino): ')
        if user == 'report':
            reporting()
        elif user == 'exit':
            exit = True
        else:
            drink_give(user)


CoffeMachine()
