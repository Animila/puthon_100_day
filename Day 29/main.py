from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# словарь
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # удаление значений в строке
    password_input.delete(0, END)

    # рандомный выбор количества букв, символов и номеров
    # перебор словарей по данному выбору
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    # Перебор словаря
    random.shuffle(password_list)

    # преобразование массива в строку
    password = "".join(password_list)

    # ввод в поле пароля
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # значения из строк в переменные
    site = website_input.get()
    password = password_input.get()
    login = login_input.get()

    # проверка на пустые строки (если пустое - выводится окно)
    # в противном случае задается вопрос о правильности введенных данных
    if site == '' or password == '' or login == '':
        messagebox.showinfo(title="ОШИБКА", message="Одна из строк пустая")
    else:
        user_var = messagebox.askyesno(title=site, message=f"Введенные ваши данные: "
                                                           f"\n\n Логин: {login}"
                                                           f"\n Пароль: {password}"
                                                           f"\n\n Вы уверены, что все верно?")

        # если все верно, то в файл записывается строка состоящая из переменных
        # а также очищается все поля
        if user_var:
            with open("password.txt", mode="a") as file:
                file.write(f"{site} | {login} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# инициализация окна
window = Tk()
window.title("Менеджер паролей")
window.config(pady=20, padx=20)

# установка логотипа
canvas = Canvas(height=200, width=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# заголовки
website_label = Label(text="Сайт:", width=20)
website_label.grid(row=1, column=0)

login_label = Label(text="Почта/ник:", width=20)
login_label.grid(row=2, column=0)

password_label = Label(text="Пароль:", width=20)
password_label.grid(row=3, column=0)

# ввод данных
website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

login_input = Entry(width=50)
login_input.grid(row=2, column=1, columnspan=2)
login_input.insert(END, "khristoforov-i@mail.ru")

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# кнопки
gen_pas = Button(text="Генерация пароля", width=14, command=generate_password)
gen_pas.grid(row=3, column=2)

save_btn = Button(text="Сохранить", width=40, command=save_password)
save_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
