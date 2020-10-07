from random import *
import turtle as t

t.speed(0)
for i in range(300):
    t.forward(randint(0, 100))
    t.left(randint(0, 360))