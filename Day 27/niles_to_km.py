from tkinter import *

# расчет
def calculation():
    km_result = float(input_miles.get()) * 1.609344
    km["text"] = round(km_result, 2)


# реализация окна (заголовок, размер и отступы)
window = Tk()
window.title("Конвертер миль в км")
window.minsize(width=200, height=100)
window.config(pady=20, padx=20)

# текст перед километрами
label = Label(text="это - ")
label.grid(column=0, row=1)

# надпись милей
label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

# надпись километров
label_km = Label(text="km")
label_km.grid(column=2, row=1)

# Ввод милей
input_miles = Entry(width=10)
input_miles.insert(END, string="0")
input_miles.grid(column=1, row=0)

# Вывод километров
km = Label(text="0")
km.grid(column=1, row=1)

# кнопка для расчета
button = Button(text="Расчет", command=calculation)
button.grid(column=1, row=2)

window.mainloop()
