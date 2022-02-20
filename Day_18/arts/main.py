import random

from get_color import rgb_colors

import turtle as t

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for count in range(1, number_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()