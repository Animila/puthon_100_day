from turtle import Turtle
import random


class Food(Turtle):
    """Класс еды (наследуется от черепахи модуля)"""

    def __init__(self):
        """Наследуем, делаем шар, поднимаем перо, размер, цвет, скорость, перенос в рандомно место"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Генерация еды"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
