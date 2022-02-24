from turtle import Turtle

# Константы
# Стартовая позиция (голова, тело, хвост)
# Размер движения блока
# Направления для поворота
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Класс работы змеи"""

    def __init__(self):
        """Массив тела, создание змеи, присвоение первого элемента в голове"""
        self.snake_seg = []
        self.create()
        self.head = self.snake_seg[0]

    def create(self):
        """Создание змеи"""

        # Цикл (проходится по стартовой позиции (с головы и до хвоста))
        # Инициализация черепахи в виде квадрата
        # Поднятие вверх ручки (чтобы не оставлять линии)
        # Цвет квадрата
        # Перенос квадрата на позицию
        # Добавление в массив тела квадрат
        for pos in START_POS:
            snake_new = Turtle('square')
            snake_new.penup()
            snake_new.color('white')
            snake_new.goto(pos)
            self.snake_seg.append(snake_new)

    def move(self):
        """Движение змеи"""

        # Цикл (проходится по длине массива тела, начиная с конца(хвоста)
        # и заканчивая головой (0) с шагом в обратную сторону)
        #
        # 1-2. находим позицию следующего блока
        # 2. двигаем текущий блок на позицию следующего блока
        #
        # Двигаем голову
        for seg_num in range(len(self.snake_seg) - 1, 0, -1):
            new_x = self.snake_seg[seg_num - 1].xcor()
            new_y = self.snake_seg[seg_num - 1].ycor()
            self.snake_seg[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
