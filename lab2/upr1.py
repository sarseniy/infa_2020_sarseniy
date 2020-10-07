import turtle as t
SIZE = 70
DIAG = SIZE * 2 ** 0.5


def draw_grid(num_of_digits):
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


def setup():
    t.penup()
    t.goto(-300, -SIZE)
    t.width(5)


def draw(number):
    if number == 0:
        zero()
    elif number == 1:
        one()
    elif number == 2:
        two()
    elif number == 3:
        three()
    elif number == 4:
        four()
    elif number == 5:
        five()
    elif number == 6:
        six()
    elif number == 7:
        seven()
    elif number == 8:
        eight()
    elif number == 9:
        nine()
    t.forward(SIZE * 1.5)


def generate_list(index):
    num_of_digits = len(index)
    order = [0] * num_of_digits
    index = int(index)
    for i in range(num_of_digits):
        order[i] = index % 10
        index //= 10
    right_order = order[::-1]
    return right_order


def zero():
    t.pendown()
    t.forward(SIZE)
    t.left(90)
    t.forward(2 * SIZE)
    t.left(90)
    t.forward(SIZE)
    t.left(90)
    t.forward(2 * SIZE)
    t.left(90)
    t.penup()


def one():
    t.forward(SIZE)
    t.pendown()
    t.left(90)
    t.forward(2 * SIZE)
    t.left(135)
    t.forward(SIZE * 2 ** 0.5)
    t.penup()
    t.left(45)
    t.forward(SIZE)
    t.left(90)


def two():
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


def three():
    t.pendown()
    t.left(45)
    t.forward(DIAG)
    t.left(135)
    t.forward(SIZE)
    t.right(135)
    t.forward(DIAG)
    t.left(135)
    t.forward(SIZE)
    t.penup()
    t.left(90)
    t.forward(2 * SIZE)
    t.left(90)


def four():
    t.forward(SIZE)
    t.left(90)
    t.pendown()
    t.forward(2 * SIZE)
    t.backward(SIZE)
    t.left(90)
    t.forward(SIZE)
    t.right(90)
    t.forward(SIZE)
    t.penup()
    t.backward(2 * SIZE)
    t.right(90)


def five():
    t.pendown()
    for j in range(2):
        t.forward(SIZE)
        t.left(90)
    for j in range(3):
        t.forward(SIZE)
        t.right(90)
    t.penup()
    t.forward(2 * SIZE)
    t.left(90)
    t.backward(SIZE)


def six():
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


def seven():
    t.pendown()
    t.left(90)
    t.forward(SIZE)
    t.right(45)
    t.forward(DIAG)
    t.left(135)
    t.forward(SIZE)
    t.left(90)
    t.penup()
    t.forward(2 * SIZE)
    t.left(90)


def eight():
    t.pendown()
    for i in range(4):
        t.forward(SIZE)
        t.left(90)
    t.left(90)
    t.forward(SIZE)
    t.right(90)
    for i in range(4):
        t.forward(SIZE)
        t.left(90)
    t.right(90)
    t.forward(SIZE)
    t.left(90)
    t.penup()


def nine():
    t.pendown()
    t.left(45)
    t.forward(DIAG)
    t.left(45)
    for i in range(4):
        t.forward(SIZE)
        t.left(90)
    t.right(45)
    t.backward(DIAG)
    t.right(45)
    t.penup()


ind = input('Введите индекс: ')
draw_grid(len(ind))
setup()

for i in generate_list(ind):
    draw(i)
