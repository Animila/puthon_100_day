import tkinter

# Инициализация
window = tkinter.Tk()
window.title("Моя первая GUI программа")
window.minsize(width=500, height=300)

# Заголовок
my_label = tkinter.Label(text="Я заголовок", font=("Arial", 24, "bold"))
my_label.pack()  # автоматическое размещение (геометрия)
# expand=(true, false) - расширение на все пространство
# side=('left', 'right', 'top', 'bottom') - сторона

# держит окно до действия
window.mainloop()
