import pygame
from pygame.draw import *


def leg(pos, size):
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(15 * size), round(40 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(33 * size), round(15 * size), round(40 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(68 * size), round(20 * size), round(11 * size)))


def lama(pos, size):
    pos[0] = round(pos[0] * size)
    pos[1] = round(pos[1] * size)
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(117 * size), round(46 * size)))
    leg((pos[0], pos[1] + round(20 * size)), size)
    leg((pos[0] + round(25 * size), pos[1] + round(30 * size)), size)
    leg((pos[0] + round(68 * size), pos[1] + round(20 * size)), size)
    leg((pos[0] + round(86 * size), pos[1] + round(35 * size)), size)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(87 * size), pos[1] - round(65 * size), round(34 * size),
                                       round(90 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(93 * size), pos[1] - round((83 * size)), round(41 * size),
                                       round(25 * size)))
    circle(screen, PURPLE, (pos[0] + round(112 * size), pos[1] - round(70 * size)), round(8 * size))
    circle(screen, BLACK, (pos[0] + round(115 * size), pos[1] - round(70 * size)), round(4 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(106 * size), pos[1] - round(75 * size), round(6 * size),
                                       round(4 * size)))
    ear1 = [pos[0] + round(96 * size), pos[1] - round(75 * size)]
    polygon(screen, WHITE, [ear1, (ear1[0] - round(15 * size), ear1[1] - round(22 * size)), (ear1[0] + round(10 * size),
                                                                                             ear1[1])])
    ear2 = [pos[0] + round(108 * size), pos[1] - round(80 * size)]
    polygon(screen, WHITE,
            [ear2, (ear2[0] - round(15 * size), ear2[1] - round(22 * size)), (ear2[0] + round(10 * size), ear2[1])])


def flower(pos, size):
    param = [15, 7]
    param[0] = round(param[0] * size)
    param[1] = round(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(12 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(5 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(5 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(9 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(9 * size), param[0], param[1]), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(13 * size), param[0], param[1]), 1)


def bush(pos, size):
    radius = 100
    circle(screen, L_GREEN, pos, round(radius * size))
    flower((pos[0] - round(5 * size), pos[1] + round(35 * size)), 1.6 * size)
    flower((pos[0] - round(70 * size), pos[1] - round(45 * size)), 1.4 * size)
    flower((pos[0] - round(30 * size), pos[1] - round(20 * size)), 1.2 * size)
    flower((pos[0] + round(10 * size), pos[1] - round(55 * size)), 1.8 * size)
    flower((pos[0] - round(75 * size), pos[1] + round(25 * size)), 1.8 * size)


RED = (255, 000, 000)
BLUE = (000, 000, 255)
GREEN = (000, 255, 000)
B_GREEN = (170, 222, 105)
L_GREEN = (112, 200, 55)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 000)
GRAY = (128, 128, 128)
BLACK = (000, 000, 000)
SKY = (185, 211, 238)
PURPLE = (229, 128, 255)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 706))

# Прорисовка фона
rect(screen, SKY, (0, 0, 500, 706))

polygon(screen, GRAY,
        [(0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122), (500, 26), (500, 706), (0, 706)])
polygon(screen, BLACK,
        [(0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122), (500, 26), (500, 706), (0, 706)],
        1)

polygon(screen, B_GREEN,
        [(0, 373), (38, 362), (75, 359), (114, 352), (271, 355), (280, 414), (294, 418), (500, 419), (500, 706),
         (0, 706)])
polygon(screen, BLACK,
        [(0, 373), (38, 362), (75, 359), (114, 352), (271, 355), (280, 414), (294, 418), (500, 419), (500, 706),
         (0, 706)], 1)

# Создание кустов
bush((420, 581), 1)
bush((110, 625), 1.2)
bush((440, 400), 0.7)


# Drawing lamas
lama([280, 600], 0.7)
lama([600, 800], 0.5)
lama([-80, 190], 3)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
