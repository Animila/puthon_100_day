import random
from hangman_words import words
from hangman_art import logo, stages

# Выбор слова
secret_text = random.choice(words)
len_text = len(secret_text)
end_of_game = False
die_count = 0

# Создание пустых клеток
display_text = []
for _ in range(len_text):
    display_text.append('_')


# преобразование клеток в пустое слово
def active_Word(list_word):
    word = ""
    for symbols in list_word:
        word += symbols
    print(word, '\n')

print(logo)
print("Добро пожаловать в игру 'Палач'")
active_Word(display_text)
# print(f'Для разработчиков: {secret_text}')
# игра длиться, пока переменная не станет положитной
while not end_of_game:
    char_user = input("Введите букву: ").lower()

    if char_user in display_text:
        print("Вы уже отгадывали это число")

    for position in range(len_text):
        char = secret_text[position]
        if char == char_user:
            display_text[position] = char


    if char_user not in secret_text:
        print(f"Вы выбрали {char_user}, но его нет в слове. Вы потеряли жизнь")
        die_count += 1

    active_Word(display_text)
    print(stages[die_count], '\n')

    if '_' not in display_text:
        end_of_game = True
        print("Ты выйграл!")

    if die_count >= 6:
        end_of_game = True
        print("Ты проиграл!")