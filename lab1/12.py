import turtle as t
from math import pi
t.speed(0)


def arc(radius, degree, direction, precision=20):
    part_of_circle = (degree / 360)
    delta = 2 * pi * radius * part_of_circle / precision
    angle_delta = (180 - 180 * (precision - 2) / precision) * part_of_circle
    if direction == 'left':
        for i in range(precision):
            t.forward(delta)
            t.left(angle_delta)
    if direction == 'right':
        for i in range(precision):
            t.forward(delta)
            t.right(angle_delta)


t.left(90)
dir = 'right'
n = 5
for i in range(n):
    for rad in 50, 10:
        arc(rad, 180, dir)