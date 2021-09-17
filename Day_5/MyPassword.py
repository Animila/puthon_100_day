import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ввод данных
print("Добро пожаловать в генератор паролей!")
nr_letters = int(input(f"Какой длины нужен пароль? (максимально {len(letters)}):\n"))
nr_symbols = int(input(f"Сколько символов добавить? (максимально {len(symbols)}):\n"))
nr_numbers = int(input(f"Сколько цифр добавить? (максимально {len(numbers)}):\n"))

# переменные:
# 1)для пароля
# 2)для списка символов

password = ''
password_list = []

# от 1 до указанного размера
# проверка на длину символов
# рандомный выбор знака
# добавления знака в список

for i in range(1, nr_letters):
    if len(password_list) < nr_letters:
        letter_random = random.randint(0, len(letters)-1)
        symbols_random = random.randint(0, len(symbols)-1)
        number_random = random.randint(0, len(numbers)-1)
        password_list.append(numbers[number_random])
        password_list.append(letters[letter_random])
        password_list.append(symbols[symbols_random])

# переброс всех знаков по длине добавления
for i in range(0, nr_letters):
    password_list[i] = password_list[random.randint(0, len(password_list)-1)]
    password += password_list[i]

print(password)
print(len(password))


