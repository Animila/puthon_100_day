import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_for():
    tim.forward(10)

screen.listen()
turtle.onkey(fun=move_for, key='space')

screen.exitonclick()