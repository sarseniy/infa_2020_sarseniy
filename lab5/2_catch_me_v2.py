import pygame
from pygame.draw import *
from random import randint
from math import cos, pi, sin, radians
pygame.init()

NUM = 3
MIN_R = 20
MAX_R = 100
WIDTH = 1200
HEIGHT = 600
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

TYPE = ['CIRCLE', 'SQUARE']

count = 0


def new_balls(num):
    """
    Функция рисует num мячиков.
    :param num: колличество мячиков
    """
    global x, y, r, v, alpha, color, type
    x = []
    y = []
    r = []
    v = []
    alpha = []
    color = []
    type = []
    for i in range(num):
        x.append(randint(MAX_R, WIDTH - MAX_R))
        y.append(randint(MAX_R, HEIGHT - MAX_R))
        r.append(randint(MIN_R, MAX_R))
        v.append(randint(10, 500))
        v[i] = float(v[i])
        alpha.append(randint(0, 360))
        alpha[i] = radians(alpha[i])
        color.append(COLORS[randint(0, 5)])
        type.append(TYPE[randint(0, 1)])
        if type[i] == 'CIRCLE':
            circle(screen, color[i], (x[i], y[i]), r[i])
        if type[i] == 'SQUARE':
            rect(screen, color[i], (x[i], y[i], r[i], r[i]))


def move_balls(num):
    """
    Функция отвечает за передвижение мячиков по экрану.
    :param num: коллическтво мячиков
    """
    global x, y, r, v, alpha, color, alpha
    for i in range(num):
        if type[i] == 'CIRCLE':
            circle(screen, BLACK, (x[i], y[i]), r[i])
        if type[i] == 'SQUARE':
            rect(screen, BLACK, (x[i], y[i], r[i], r[i]))
        '''x[i] += round(v[i] / FPS * cos(alpha[i]))
        y[i] -= round(v[i] / FPS * sin(alpha[i]))'''
        if type[i] == 'CIRCLE':
            x[i] += round(v[i] / FPS * cos(alpha[i]))
            y[i] -= round(v[i] / FPS * sin(alpha[i]))
            circle(screen, color[i], (x[i], y[i]), r[i])
        if type[i] == 'SQUARE':
            v[i] *= randint(90, 110) / 100
            alpha[i] += radians(randint(0, 10) - 5)
            x[i] += round(v[i] / FPS * cos(alpha[i]))
            y[i] -= round(v[i] / FPS * sin(alpha[i]))
            rect(screen, color[i], (x[i], y[i], r[i], r[i]))
        pygame.display.update()
    check_walls(num)


def check_walls(num):
    """
    Функция проверяет удар мячика о стенку и считает новый угол
    :param num: колличество мячиков
    """
    global x, y, r, alpha
    for i in range(num):
        if type[i] == 'CIRCLE':
            if x[i] + r[i] > WIDTH - 10:
                alpha[i] = radians(90 + randint(10, 170))
            if x[i] - r[i] < 0 + 10:
                alpha[i] = radians(randint(10, 170) - 90)
            if y[i] + r[i] > HEIGHT - 10:
                alpha[i] = radians(randint(10, 170))
            if y[i] - r[i] < 0 + 10:
                alpha[i] = radians(randint(10, 170) - 180)
        if type[i] == 'SQUARE':
            if x[i] + r[i] > WIDTH - 10:
                alpha[i] = radians(90 + randint(10, 170))
            if x[i] < 0 + 10:
                alpha[i] = radians(randint(10, 170) - 90)
            if y[i] + r[i] > HEIGHT - 10:
                alpha[i] = radians(randint(10, 170))
            if y[i] < 0 + 10:
                alpha[i] = radians(randint(10, 170) - 180)
        alpha[i] %= 2 * pi


def respawn_figure(i):
    """
    Функция заново создаёт мишень после попадания в цель.
    :param i: номер "возрождаемого" элемента
    """
    x[i] = randint(MAX_R, WIDTH - MAX_R)
    y[i] = randint(MAX_R, HEIGHT - MAX_R)
    r[i] = randint(MIN_R, MAX_R)
    v[i] = randint(10, 500)
    alpha[i] = randint(0, 360)
    alpha[i] = radians(alpha[i])
    color[i] = COLORS[randint(0, 5)]
    type[i] = TYPE[randint(0, 1)]
    if type == 'CIRCLE':
        circle(screen, color[i], (x[i], y[i]), r[i])
    if type == 'SQUARE':
        rect(screen, color[i], (x[i], y[i], r[i], r[i]))
    pygame.display.update()


def check_click(event, num):
    """
    Функция проверяет, попал ли игрок по мячику, подсчитывает очки и рисует новые мячики при необходимости.
    :param event: параметры события
    :param num: колличество мячиков
    """
    global count, x, y, r, v, alpha, color
    coord = event.pos
    for i in range(num):
        if type[i] == 'CIRCLE':
            if (x[i] - coord[0]) ** 2 + (y[i] - coord[1]) ** 2 <= r[i] ** 2:
                count += 1
                circle(screen, BLACK, (x[i], y[i]), r[i])
                print(count)

                respawn_figure(i)
        if type[i] == 'SQUARE':
            if 0 <= coord[0] - x[i] <= r[i] and 0 <= coord[1] - y[i] <= r[i]:
                count += 3
                rect(screen, BLACK, (x[i], y[i], r[i], r[i]))
                print(count)

                respawn_figure(i)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    new_balls(NUM)
    pygame.display.update()
    f = True
    while f:
        clock.tick(FPS)
        move_balls(NUM)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event, NUM)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()