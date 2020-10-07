import turtle as t


t.shape('turtle')
start = 10
delta = 10
number = 10
end = start + delta * (number + 1)
for length in range(start, end, delta):
    t.forward(length)
    t.left(90)
