import turtle as t
import random

tim = t.Turtle()

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']


def draw_shape(num_shape):
    angle = 360 / num_shape
    for _ in range(num_shape):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# tim.pencolor('blue')
# for _ in range(3):
#     tim.right(120)
#     tim.forward(100)
#
# tim.pencolor('black')
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
#
# tim.pencolor('red')
# for _ in range(5):
#     tim.right(72)
#     tim.forward(100)
#
# tim.pencolor('green')
# for _ in range(6):
#     tim.right(60)
#     tim.forward(100)
#
# tim.pencolor('pink')
# for _ in range(7):
#     tim.right(51.43)
#     tim.forward(100)
#
# for _ in range(8):
#     tim.right(45)
#     tim.forward(100)
#
# for _ in range(9):
#     tim.right(40)
#     tim.forward(100)
