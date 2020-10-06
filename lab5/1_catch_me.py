import pygame
from pygame.draw import *
from random import randint
from math import cos, pi, sin, radians
pygame.init()

MIN_R = 10
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

count = 0


def new_ball():
    """
    Функция рисует новый шарик на экране.
    """
    global x, y, r, v, alpha, color
    x = randint(MAX_R, WIDTH - MAX_R)
    y = randint(MAX_R, HEIGHT - MAX_R)
    r = randint(MIN_R, MAX_R)
    v = randint(10, 500)
    alpha = randint(0, 360)
    alpha = radians(alpha)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_ball_2():
    """
    Функция рисует новый шарик на экране.
    """
    global x2, y2, r2, v2, alpha2, color2
    x2 = randint(MAX_R, WIDTH - MAX_R)
    y2 = randint(MAX_R, HEIGHT - MAX_R)
    r2 = randint(MIN_R, MAX_R)
    v2 = randint(10, 500)
    alpha2 = randint(0, 360)
    alpha2 = radians(alpha2)
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x2, y2), r2)


def check_walls2():
    """
    Функция проверяет столкновение шарика с краями экрана и изменяет направление его движения при необходимости.
    """
    global x2, y2, r2, alpha2
    if x2 + r2 > WIDTH - 10:
        alpha2 = pi - alpha2
    if x2 - r2 < 0 + 10:
        alpha2 = pi - alpha2
    if y2 + r2 > HEIGHT - 10:
        alpha2 = 2 * pi - alpha2
    if y2 - r2 < 0 + 10:
        alpha2 = 2 * pi - alpha2
    alpha2 %= 2 * pi


def move_ball2():
    global x2, y2, r2, v2, alpha2, color2
    circle(screen, BLACK, (x2, y2), r2)
    x2 += round(v2 / FPS * cos(alpha2))
    y2 -= round(v2 / FPS * sin(alpha2))
    circle(screen, color2, (x2, y2), r2)
    pygame.display.update()
    check_walls2()


def check_walls():
    """
    Функция проверяет столкновение шарика с краями экрана и изменяет направление его движения при необходимости.
    """
    global x, y, r, alpha
    if x + r > WIDTH - 10:
        alpha = pi - alpha
    if x - r < 0 + 10:
        alpha = pi - alpha
    if y + r > HEIGHT - 10:
        alpha = 2 * pi - alpha
    if y - r < 0 + 10:
        alpha = 2 * pi - alpha
    alpha %= 2 * pi


def move_ball():
    global x, y, r, v, alpha, color
    circle(screen, BLACK, (x, y), r)
    x += round(v / FPS * cos(alpha))
    y -= round(v / FPS * sin(alpha))
    circle(screen, color, (x, y), r)
    pygame.display.update()
    check_walls()


def check_click(event):
    """
    Функция проверяет, попал ли игрок мышью по шарику.
    :param event: параметры события
    :return: возвращает логическую переменную в зависимости от того, было попадание или нет
    """
    global count
    coord = event.pos
    if (x - coord[0]) ** 2 + (y - coord[1]) ** 2 <= r ** 2:
        count += 1
        print(count)
        return True
    else:
        return False


def check_click2(event):
    """
    Функция проверяет, попал ли игрок мышью по шарику.
    :param event: параметры события
    :return: возвращает логическую переменную в зависимости от того, было попадание или нет
    """
    global count
    coord = event.pos
    if (x2 - coord[0]) ** 2 + (y2 - coord[1]) ** 2 <= r2 ** 2:
        count += 1
        print(count)
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    new_ball()
    new_ball_2()
    pygame.display.update()
    f = True
    while f:
        clock.tick(FPS)
        move_ball()
        move_ball2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if check_click(event):
                    circle(screen, BLACK, (x, y), r)
                    new_ball()
                if check_click2(event):
                    circle(screen, BLACK, (x2, y2), r2)
                    new_ball_2()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
