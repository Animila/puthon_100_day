print('Добро пожаловать в калькулятор чаевых')
bill = float(input('Какой общий счет? $'))
percent = int(input('Какой процентр вы бы хотели дать в чаевых? (10, 12, 15) '))
count = int(input("Сколько вас? "))

# смотрим сколько чаевых должны
percent_bill = bill / 100 * percent

# ищем общую сумму денег
sum_bill = round((bill + percent_bill) / count, 2)

print(f"Каждый должен заплатить: ${sum_bill}")
