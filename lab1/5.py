import turtle as t


def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


delta = 20
for a in range(delta, 11 * delta, delta):
    square(a)
    t.right(135)
    t.penup()
    t.forward(delta / (2 ** 0.5))
    t.left(135)
    t.pendown()