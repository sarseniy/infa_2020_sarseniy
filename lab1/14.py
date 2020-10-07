import turtle as t


def star(number, length = 100):
    for i in range(number):
        t.forward(length)
        t.left(180 - 180 / number)


t.shape('turtle')

t.left(180)
star(5)
t.penup()
t.left(180)
t.forward(150)
t.left(180)
t.pendown()

star(11)
