import turtle as t
from turtle import Screen
screen = Screen()
SIZE = 70
DIAG = SIZE * 2 ** 0.5
file = open('ways', 'r')
info = file.readlines()
for i in range(len(info)):
    info[i] = info[i].rstrip()


def setup():
    t.penup()
    t.goto(-300, -SIZE)
    t.width(5)


def generate_list(index):
    num_of_digits = len(index)
    order = [0] * num_of_digits
    index = int(index)
    for i in range(num_of_digits):
        order[i] = index % 10
        index //= 10
    right_order = order[::-1]
    return right_order


def draw(digit):
    result = open('paste.py', 'w')
    if digit == 0:
        digit_str = 'zero'
    elif digit == 1:
        digit_str = 'one'
    elif digit == 2:
        digit_str = 'two'
    elif digit == 3:
        digit_str = 'three'
    elif digit == 4:
        digit_str = 'four'
    elif digit == 5:
        digit_str = 'five'
    elif digit == 6:
        digit_str = 'six'
    elif digit == 7:
        digit_str = 'seven'
    elif digit == 8:
        digit_str = 'eight'
    elif digit == 9:
        digit_str = 'nine'
    command = ''
    print(info)
    flag = False
    for x in info:
        if x == 'def ' + digit_str + '():':
            flag = True
            #command = command + x + '\n'
            continue
        if flag:
            command = command + x + '\n'
        if flag and x == '':
            #eval(''command)
            break
    result.write('SIZE = 70\n' + 'DIAG = SIZE * 2 ** 0.5\n' + 'import turtle as t\n' + 'def action():\n' + command)
    result.close()
    result = open('paste.py', 'r')
    import paste
    paste.action()
    result.close()


ind = input('Введите индекс: ')
print(generate_list(ind))
setup()
for i in generate_list(ind):
    draw(i)
screen.exitonclick()
