import turtle as t
from turtle import Screen
screen = Screen()
SIZE = 50
DIAG = SIZE * 2 ** 0.5


def draw_grid(num_of_digits):
    t.speed(0)
    t.penup()
    t.goto(-300, -SIZE)
    t.pendown()
    t.width(1)
    for k in range(4):
        for j in range(num_of_digits * 2 + num_of_digits - 1):
            for h in range(4):
                t.forward(SIZE / 2)
                t.left(90)
            if j % 3 == k % 2:
                t.left(45)
                t.forward(DIAG / 2)
                t.backward(DIAG / 2)
                t.right(45)
            t.forward(SIZE / 2)
        t.penup()
        t.goto(-300, -SIZE)
        t.pendown()
        t.left(90)
        t.forward((k + 1) * SIZE / 2)
        t.right(90)


def generate_list(index):
    num_of_digits = len(index)
    order = [0] * num_of_digits
    index = int(index)
    for i in range(num_of_digits):
        order[i] = index % 10
        index //= 10
    right_order = order[::-1]
    return right_order


def setup():
    t.speed(5)
    t.penup()
    t.goto(-300, -SIZE)
    t.width(5)


def line(num):
    d1 = {0: [0, 2, 1, 2],
          1: [0, 1, 0, 2],
          2: [0, 1, 1, 2],
          3: [1, 1, 1, 2],
          4: [0, 1, 1, 1],
          5: [0, 0, 0, 1],
          6: [0, 0, 1, 1],
          7: [1, 0, 1, 1],
          8: [0, 0, 1, 0]}
    x0, y0, x1, y1 = d1[num]
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(x_start + SIZE * x0, y_start + y0 * SIZE)
    t.pendown()
    t.goto(x_start + SIZE * x1, y_start + SIZE * y1)
    t.penup()
    t.goto(x_start, y_start)


"""def _zero():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor() + 2 * SIZE)
    t.pendown()
    t.goto(t.xcor() + SIZE, t.ycor())
    t.penup()
    t.goto(x_start, y_start)


def _first():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.pendown()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _second():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.pendown()
    t.goto(t.xcor() + SIZE, t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _third():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor() + SIZE, t.ycor() + SIZE)
    t.pendown()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _fourth():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.pendown()
    t.goto(t.xcor() + SIZE, t.ycor())
    t.penup()
    t.goto(x_start, y_start)


def _fifth():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor())
    t.pendown()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _sixth():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor())
    t.pendown()
    t.goto(t.xcor() + SIZE, t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _seventh():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor() + SIZE, t.ycor())
    t.pendown()
    t.goto(t.xcor(), t.ycor() + SIZE)
    t.penup()
    t.goto(x_start, y_start)


def _eigth():
    x_start = t.xcor()
    y_start = t.ycor()
    t.penup()
    t.goto(t.xcor(), t.ycor())
    t.pendown()
    t.goto(t.xcor() + SIZE, t.ycor())
    t.penup()
    t.goto(x_start, y_start)"""

"""dictionary = {'0': [5, 1, 0, 3, 7, 8],
              '1': [2, 3, 7],
              '2': [0, 3, 6, 8],
              '3': [0, 2, 4, 6],
              '4': [1, 4, 3, 7],
              '5': [0, 1, 4, 7, 8],
              '6': [2, 4, 7, 8, 5],
              '7': [0, 2, 5],
              '8': [1, 0, 3, 4, 5, 7, 8],
              '9': [1, 0, 3, 4, 6]}"""

coordinates = {}
info = open('text', 'r')
for i, _line in enumerate(info):
    coordinates[i] = [int(num) for num in _line.split()]


info.close()
ind = input()
draw_grid(len(ind))
setup()
a = generate_list(ind)
for i in a:
    for number in coordinates[i]:
        line(number)
    t.forward(SIZE * 1.5)

screen.exitonclick()
