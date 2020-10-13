SIZE = 70
DIAG = SIZE * 2 ** 0.5
import turtle as t
def action():
    t.pendown()
    for i in range(4):
        t.forward(SIZE)
        t.left(90)
    t.left(90)
    t.forward(SIZE)
    t.right(45)
    t.forward(DIAG)
    t.backward(DIAG)
    t.left(45)
    t.backward(SIZE)
    t.right(90)
    t.penup()

