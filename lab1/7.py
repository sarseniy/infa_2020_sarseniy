from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(2000):
    t = i / 20 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)