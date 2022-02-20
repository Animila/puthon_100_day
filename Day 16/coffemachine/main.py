from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
exit = False


while not exit:
    option = menu.get_items()
    user = input(f'Что бы вы хотели? ({option}):')
    if user == 'off':
        exit = True
    elif user == 'report':
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(user)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)