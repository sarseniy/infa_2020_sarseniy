import turtle as t
from math import pi, sin


def polygon_size(radius, number):
    return 2 * radius * sin(pi / number)


def polygon(length, number):
    angle = 180 - 180 * (number - 2) / number
    angle_2 = 180 - 180 * (number - 2) / (2 * number)
    t.left(angle_2)
    for i in range(number):
        t.forward(length)
        t.left(angle)
    t.right(angle_2)

n = 10
delta_r = 10
for i in range(3, n + 3):
    t.penup()
    t.forward(delta_r)
    t.pendown()
    length = polygon_size(delta_r * (i - 2), i)
    polygon(length, i)
