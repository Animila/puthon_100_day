import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
count_active = 0
timer_count = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # остановка функции подсчета
    # обнуление таймера
    # обнуление галок
    # Возврат заголовка
    window.after_cancel(timer_count)
    canvas.itemconfig(time_text, text="00:00")
    succeed.config(text="")
    title.config(text="Таймер", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # количество запусков таймера
    global count_active
    count_active += 1
    print(count_active)

    # перевод в секунды
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Если это 8 запуск (или 4 перерыв) - долгий отдых
    if count_active % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Отдых", fg=RED)
    # Малый отдых при каждом втором запуске
    elif count_active % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Отдых", fg=PINK)
    # Просто запуск по работе
    else:
        count_down(work_sec)
        title.config(text="Работа", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # подсчет минут и секунд
    # проверка на числа до 10 с добавлением нуля впереди
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    if min < 10:
        min = f'0{min}'

    # строка таймера из обоих переменных
    # приравнивание к тексту таймера строки таймера
    time_count = f"{min}:{sec}"
    canvas.itemconfig(time_text, text=time_count)

    # Пока работает таймер, но сам себя вызывает в конце 1 секунды
    # По окончании снова запускается и добавляет новую галку в конце, если это рабочий таймер
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        mark = " "
        work_session = math.floor(count_active / 2)
        for _ in range(work_session):
            mark += "✔"
        succeed.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# инициализация
window = Tk()
window.title("Помидор")
window.config(padx=100, pady=50, bg=YELLOW)

# заголовок
title = Label(text="Таймер", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
title.grid(column=1, row=0)

# слои
# указание типа файла
# захват изображения
# текст таймера
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
time_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# элементы
# кнопка пуска
start = Button(text="Запуск", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# кнопка перезапуска
reset = Button(text="Сброс", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# галки
succeed = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
succeed.grid(column=1, row=3)

window.mainloop()
