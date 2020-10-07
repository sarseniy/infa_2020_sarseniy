import turtle as t
from turtle import Screen
screen = Screen()
'''from math import pi
t.speed(0)


def half_of_circle(radius, direction, precision=20):
    delta = 2 * pi * radius / precision
    angle_delta = 360 / precision
    if direction == 'left':
        for i in range(precision // 2):
            t.forward(delta)
            t.left(angle_delta)
    if direction == 'right':
        for i in range(precision // 2):
            t.forward(delta)
            t.right(angle_delta)
'''

t.left(90)
t.goto(500, 0)
t.goto(0, 0)

dir = 'right'
n = 4
for i in range(n):
    for rad in 50, 10:
        t.circle(-rad, 180)

screen.exitonclick()