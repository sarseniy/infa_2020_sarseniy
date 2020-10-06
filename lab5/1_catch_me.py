import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 600))

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
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def check_click(event):
    """
    Функция проверяет, попал ли игрок мышью по шарику.
    :param event: параметры события
    """
    global count
    coord = event.pos
    if (x - coord[0]) ** 2 + (y - coord[1]) ** 2 <= r ** 2:
        count += 1
        print(count)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click(event)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
