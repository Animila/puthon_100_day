from turtle import Screen, Turtle
from Block import Block
from ball import Ball
from scoreboard import Scoryboard
import time

# настройка экрана
screen = Screen()
screen.bgcolor('black')
screen.title('Пинг понг')
screen.setup(width=800, height=600)
screen.tracer(0)

# создание блоков
r_block = Block(370, 0)
l_block = Block(-370, 0)
ball = Ball()
scoreboard = Scoryboard()

# проверка на нажатие клавиш
screen.listen()
screen.onkeypress(r_block.go_up, 'Up')
screen.onkeypress(r_block.go_down, 'Down')
screen.onkeypress(l_block.go_up, 'w')
screen.onkeypress(l_block.go_down, 's')

# При установке анимации (tracer), требуется обновлять экран постоянно
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # проверка на попадание в окно (отскок)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # проверка на попадание в блок
    if ball.distance(r_block) < 50 and ball.xcor() > 340 or ball.distance(l_block) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # проверка на промах
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# закрытие окна
screen.exitonclick()
