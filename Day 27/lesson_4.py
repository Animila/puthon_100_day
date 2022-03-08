from tkinter import *

window = Tk()
window.title("Моя первая GUI программа")
window.minsize(width=500, height=300)

my_label = Label(text="Я заголовок", font=("Arial", 24, "bold"))
my_label.pack()

# # изменение текста внутри
# my_label['text'] = "hello"
# my_label.config(text="New text")


# Кнопка
def button_clicked():
    # получение данных с ввода
    my_label['text'] = input.get()


button = Button(text="Нажми на меня", command=button_clicked)
button.pack()

# ввод данных
input = Entry(width=10)
input.pack()

window.mainloop()
