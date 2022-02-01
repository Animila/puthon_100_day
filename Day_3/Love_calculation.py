print("Welcome to the Love Calculation!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

names = name1 + name2

count_2 = names.count("l")
count_2 += names.count("o")
count_2 += names.count("v")
count_2 += names.count("e")

count_1 = names.count("t")
count_1 += names.count("r")
count_1 += names.count("u")
count_1 += names.count("e")

count = int(str(count_1)+str(count_2))

if count < 10:
    print(f"Ваш результат {count}%, попробуй найти другую половинку")
elif 40 <= count <= 50:
    print(f'Ваш результат {count}%, вам хорошо вместе')
elif count >= 90:
    print(f'Ваш результат {count}%. Вы убиваете вместе')
else:
    print(f'Ваш результат {count}%')


print(count)

# Arianna Rebolini
# What is their name?
# Channing Tatum
