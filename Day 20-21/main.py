from scoreboard import Table
from turtle import Screen
from snake import Snake
from food import Food
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
score = Table()
snake = Snake()
food = Food()

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

    # Проверка на попадание еды в змею
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Проверка на столкновение
    if snake.head.xcor() > 390 or snake.head.xcor() < -410 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # проверка на столкновение
    # цикл по всем сегментам (кроме 1)
    # Если голова сталкивается с какой-либо части тела
    # То срабатывает конец игры
    for segment in snake.snake_seg[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()

screen.exitonclick()
