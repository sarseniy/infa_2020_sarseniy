SIZE = 70
DIAG = SIZE * 2 ** 0.5
import turtle as t
def action():
    t.pendown()
    t.forward(SIZE)
    t.backward(SIZE)
    t.left(45)
    t.forward(SIZE * 2 ** 0.5)
    t.left(45)
    t.forward(SIZE)
    t.left(90)
    t.forward(SIZE)
    t.penup()
    t.left(90)
    t.forward(2 * SIZE)
    t.left(90)

