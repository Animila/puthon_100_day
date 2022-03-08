from tkinter import *

window = Tk()
window.title("Помидор")
window.config(padx=100, pady=50)


def say_something(thing):
    print(thing)


# вызов функции после окончания времени (бесконечное количество аргументов)
window.after(1000, say_something, "hello")

window.mainloop()
