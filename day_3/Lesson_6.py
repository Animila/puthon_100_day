print("Добро пожаловать в любовный кулькулятор")

name1 = input("Какое ваше имя? \n")
name2 = input("Какое имя партнера\n")

name = name1.upper() + name2.upper()

love_counter = name.count('Л') + name.count('Ю') + name.count('Б') + name.count('О') + name.count('В') + name.count('Ь')
true_counter = name.count('И') + name.count('С') + name.count('Т') + name.count('И') + name.count('Н') + name.count('А')

counter = str(true_counter) + str(love_counter)

if int(counter) > 90:
    print(f"О, ваши имена совпадают на {counter}%. Вы определенно станете парой!")
elif int(counter) < 10:
    print(f"Ваши имена совпадают на {counter}%. Прости")
elif 40 < int(counter) < 50:
    print(f"Ваши имена совпадают на {counter}%. Есть шанс!")
else: 
    print(f"Ваши имена совпадают на {counter}%")
