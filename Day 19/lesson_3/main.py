import turtle
from turtle import  Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user = screen.textinput(title='Сделай свою ставку', prompt='Какая черепаха станет первой? Введите цвет')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[index])
    all_turtles.append(new_turtle)

if user:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user:
                print(f'Ты победил. {winning_color} оказался победителем')
            else:
                print(f'Ты проиграл. {winning_color} оказался победителем')

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()