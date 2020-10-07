import turtle as t
import math as m
t.speed(0)


def circle(radius, direction, precision=20):
    if direction == 'left':
        for i in range(precision):
            t.forward(2 * m.pi * radius / precision)
            t.left(180 - 180 * (precision - 2) / precision)
    if direction == 'right':
        for i in range(precision):
            t.forward(2 * m.pi * radius / precision)
            t.right(180 - 180 * (precision - 2) / precision)


t.left(90)
for rad in range(50, 210, 10):
    for dir in 'left', 'right':
        circle(rad, dir)