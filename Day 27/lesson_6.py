from tkinter import *


def clicked_label():
    print("Нажата кнопка")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Текст")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

my_label = Label(text="Заголовок", font=("Arial", 24, "bold"))
my_label.config(text="новый текст")
my_label.grid(column=0, row=0)
# my_label.place(x=100, y=0)

button = Button(text="Нажми на меня", command=clicked_label)
button.grid(column=1, row=1)

button2 = Button(text="новая", command=clicked_label)
button2.grid(column=2, row=0)

input = Entry(width=30)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
