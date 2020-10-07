import turtle as t


def leg(length):
    t.forward(length)
    t.stamp()
    t.backward(length)


t.shape('turtle')
n = 50
length = 100
for i in range(n):
    leg(length)
    t.right(360 / n)