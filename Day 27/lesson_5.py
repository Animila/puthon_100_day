from tkinter import *

window = Tk()
window.title("Виджеты")
window.minsize(width=500, height=500)

# Заголовок
label = Label(text="Это старый текст")
label.config(text="Это новый текст")
label.pack()


# Кнопки
def action():
    print("Что-то делает")
button = Button(text="Нажми на меня", command=action)
button.pack()

# Ввод
entry = Entry(width=30)
entry.insert(END, string="Какой-то текст для помощи")
print(entry.get())
entry.pack()

# Поле текста
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Просто какой-то текст")
print(text.get("1.0", END))
text.pack()


# Счетчик
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Шкала
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Галка
def check_used():
    print(check_state.get())

# проверка нажатия
check_state = IntVar()
# пункт для галки
check_button = Checkbutton(text="Это включено?", variable=check_state, command=check_used)
check_state.get()
check_button.pack()

# Выбор галки
def radio_used():
    print(radio_state.get())
# проверка нажатия
radio_state = IntVar()
# пункты
radiobutton1 = Radiobutton(text="Выбор 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Выбор 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# лист
def list_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", list_used)
listbox.pack()
window.mainloop()
