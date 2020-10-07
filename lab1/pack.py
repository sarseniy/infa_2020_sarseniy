import turtle as t
from math import pi, sin


def star(number, length = 100):
    for i in range(number):
        t.forward(length)
        t.left(180 - 180 / number)


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
