import turtle as t
t.shape('turtle')


def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


square(50)