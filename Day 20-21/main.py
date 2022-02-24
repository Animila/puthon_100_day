from turtle import Screen
from snake import Snake
import time

# Инициализация окна
# настройка размера
# цвет фона
# заголовка окна
# включение анимации и установки задержки между кадрами
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Змейка')
screen.tracer(0)

# создание змейки
snake = Snake()

# прослушивание нажатия кнопок
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


# реализация игры
# бесконечный цикл
# обновление экрана
# откладываем движение змейки на 0.1 секунду
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()








screen.exitonclick()