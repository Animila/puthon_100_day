from turtle import Turtle

# Константы для текста
ALIGHT = "center"
FONT = ("Arial", 24, "normal")


class Table(Turtle):
    """Количество очков (наследует черепаху)"""
    def __init__(self):
        """Наследует, спрятать, поднять, цвет, расположение, очки, обновление"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        """Вывод очков"""
        self.write(f"Текущий счет: {self.score}", align=ALIGHT, font=FONT)

    def increase_score(self):
        """Прибавляет к очкам 1"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("КОНЕЦ ИГРЫ", align=ALIGHT, font=FONT)
