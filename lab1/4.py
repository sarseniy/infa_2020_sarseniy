import turtle as t
import math as m


def circle(radius, direction, precision=200):
    if direction == 'left':
        for i in range(precision):
            t.forward(2 * m.pi * radius / precision)
            t.left(180 - 180 * (precision - 2) / precision)
    if direction == 'right':
        for i in range(precision):
            t.forward(2 * m.pi * radius / precision)
            t.right(180 - 180 * (precision - 2) / precision)


rad = 50
t.penup()
t.forward(rad)
t.left(90)
t.pendown()
circle(rad, 'left')