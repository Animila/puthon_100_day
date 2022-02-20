from Day_16.lesson_1 import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen

timmi = Turtle()
print(timmi)
timmi.shape("turtle")
timmi.color('red')
timmi.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()