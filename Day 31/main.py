from tkinter import *
import pandas
import random

# константа для заднего цвета
# словарь из перевода и значения
# настройки словаря
BACKGROUND_COLOR = "#B1DDC6"
learn_word = {}
LEARN_LANG = "French"
YOUR_LANG = "English"

# пытается выгрузить данные из таблицы
# если не получается - выгружаем полную таблицу в словарь
# если получилось - выгружаем полученную таблицу в словарь
try:
    data = pandas.read_csv("words_to_learn_.csv")
except FileNotFoundError:
    new_data = pandas.read_csv(f"{LEARN_LANG}_words.csv")
    learn_words = new_data.to_dict(orient="records")
else:
    learn_words = data.to_dict(orient="records")


def next_card():
    global learn_word, flip_time
    # при переходе к новой карте отменяем таймер
    # вытаскиваем слово из словаря
    # выводим значение из словаря
    # запускаем таймер за 3 секунды, потом переворот карты
    window.after_cancel(flip_time)
    learn_word = random.choice(learn_words)
    canvas.itemconfig(title, text=LEARN_LANG, fill="black")
    canvas.itemconfig(descr, text=learn_word[LEARN_LANG], fill="black")
    canvas.itemconfig(bg_card, image=front_photo)
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    global learn_word
    # вывод значения из словаря
    # смена фоновой картинки
    canvas.itemconfig(title, text=YOUR_LANG, fill="white")
    canvas.itemconfig(descr, text=learn_word[YOUR_LANG], fill="white")
    canvas.itemconfig(bg_card, image=back_photo)


def current():
    # удаляет из списка текущее слово (ключ)
    # вводит данные в таблицу без дополнительных индексов
    # запускается следующая карта
    learn_words.remove(learn_word)
    print(len(learn_words))
    data = pandas.DataFrame(learn_words)
    data.to_csv("words_to_learn_.csv", index=False)
    next_card()


# инициализация окна
window = Tk()
window.title("Карточки")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# фотографии для заднего и переднего фона карт
# и для кнопок
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
dislike_image = PhotoImage(file="images/wrong.png")
like_image = PhotoImage(file="images/right.png")

# запуск таймера при первой карте
flip_time = window.after(3000, func=flip_card)

# настраиваем слои
# устанавливаем фон
# настраиваем текст
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_card = canvas.create_image(400, 263, image=front_photo)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
descr = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# кнопки для проверки пользователя
dislike_btn = Button(image=dislike_image, relief="solid", border=0, highlightthickness=0, command=next_card)
dislike_btn.grid(row=1, column=0)
like_btn = Button(image=like_image, relief="solid", border=0, highlightthickness=0, command=current)
like_btn.grid(row=1, column=1)

# переворачиваем первую карту
next_card()

window.mainloop()
