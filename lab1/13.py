import turtle as t
from math import pi


def arc(radius, degree, direction, precision=200):
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


d = 120

t.color('black', 'yellow')
t.begin_fill()
arc(d / 2, 360, 'left')
t.end_fill()

t.penup()
t.goto(- d / 4, 5 * d / 8)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
arc(d / 16, 360, 'left')
t.end_fill()

t.penup()
t.goto(d / 4, 5 * d / 8)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
arc(d / 16, 360, 'left')
t.end_fill()

t.penup()
t.goto(0, d * 0.55)
t.pendown()

t.color('black', 'blue')
t.pensize(10)
t.goto(0, d * 0.3)

t.color('red', 'blue')
t.penup()
t.goto(d / 4, 3 * d / 8)
t.pendown()

t.right(90)
arc(d / 4, 180, 'right')
