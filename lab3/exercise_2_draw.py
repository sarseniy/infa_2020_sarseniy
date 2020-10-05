import pygame
from random import randint
from pygame.draw import *

# Цвета, используемые при рисовании графических примитивов
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


def landskape(mountains, grass):
    '''
    Функция рисует ландшафт (горы и землю).
    mountains - список пар целочисленных значений, задающих координаты вершин многоугольника, изображающего горы
    grass - список пар целочисленных значений, задающих координаты вершин многоугольника, изображающего землю
    '''
    polygon(screen, GRAY, mountains)
    polygon(screen, BLACK, mountains, 1)
    polygon(screen, B_GREEN, grass)
    polygon(screen, BLACK, grass, 1)


def leg(pos, size, reverse=False):
    '''
    Функция рисует ноги ламы.
    pos - список из двух целочисленных значений, задающих координаты левого верхнего угла верхнего эллипса, входящего в
      рисунок ноги
    size - вещественный параметр, служащий коэффициентом относительного размера
    reverse - логический параметр, определяющий сторону, на которую ориентируется нога: False - вправо (по умолчанию),
      True - влево
    '''
    if not reverse:
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(33 * size), round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(68 * size), round(20 * size), round(11 * size)))
    else:
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(15 * size), pos[1], round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(15 * size), pos[1] + round(33 * size), round(15 * size),
                                           round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(20 * size), pos[1] + round(68 * size), round(20 * size),
                                           round(11 * size)))


def draw_lama(pos, size, reverse=False):
    '''
    Функция рисует ламу.
    pos - список из двух целочисленных значений, задающих координаты опорной точки для рисования ламы; данной точкой
      служит один из верхних углов прямоугольника, в который вписывается эллипс, изображающий тело ламы; выбор
      конкретного угла (левого или правого) зависит от стороны, на которую ориентируется лама
    size - вещественный параметр, служащий коэффициентом относительного размера
    reverse - логический параметр, определяющий сторону, в которую смотрит лама: False - вправо (по умолчанию),
      True - влево
    '''
    if not reverse:
        lama_right(pos, size)
    else:
        lama_left(pos, size)


def lama_right(pos, size):
    '''
    Функция рисует ламу, которая смотрит вправо.
    pos - список из двух целочисленных значений, задающих координаты левого верхнего угла прямоугольника, в который
      вписывается эллипс, изображающий тело ламы
    size - вещественный параметр, служащий коэффициентом относительного размера
    '''
    reverse = False
    pos[0] = round(pos[0] * size)
    pos[1] = round(pos[1] * size)
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(117 * size), round(46 * size)))

    leg((pos[0], pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] + round(25 * size), pos[1] + round(30 * size)), size, reverse)
    leg((pos[0] + round(68 * size), pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] + round(86 * size), pos[1] + round(35 * size)), size, reverse)

    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(87 * size), pos[1] - round(65 * size), round(34 * size),
                                       round(90 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(93 * size), pos[1] - round((83 * size)), round(41 * size),
                                       round(25 * size)))

    circle(screen, PURPLE, (pos[0] + round(112 * size), pos[1] - round(70 * size)), round(8 * size))
    circle(screen, BLACK, (pos[0] + round(115 * size), pos[1] - round(70 * size)), round(4 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(106 * size), pos[1] - round(75 * size), round(6 * size),
                                       round(4 * size)))

    ear1 = [pos[0] + round(96 * size), pos[1] - round(75 * size)]
    polygon(screen, WHITE, [ear1, (ear1[0] - round(15 * size), ear1[1] - round(22 * size)),
                            (ear1[0] + round(10 * size), ear1[1])])
    ear2 = [pos[0] + round(108 * size), pos[1] - round(80 * size)]
    polygon(screen, WHITE,
            [ear2, (ear2[0] - round(15 * size), ear2[1] - round(22 * size)), (ear2[0] + round(10 * size), ear2[1])])


def lama_left(pos, size):
    '''
    Функция рисует ламу, которая смотрит влево.
    pos - список из двух целочисленных значений, задающих координаты правого верхнего угла прямоугольника, в который
      вписывается эллипс, изображающий тело ламы
    size - вещественный параметр, служащий коэффициентом относительного размера
    '''
    reverse = True
    pos[0] = round(pos[0] * size)
    pos[1] = round(pos[1] * size)
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(117 * size), pos[1], round(117 * size), round(46 * size)))

    leg((pos[0], pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] - round(25 * size), pos[1] + round(30 * size)), size, reverse)
    leg((pos[0] - round(68 * size), pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] - round(86 * size), pos[1] + round(35 * size)), size, reverse)

    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(87 * size) - round(34 * size), pos[1] - round(65 * size),
                                       round(34 * size), round(90 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(93 * size) - round(41 * size), pos[1] - round((83 * size)),
                                       round(41 * size), round(25 * size)))

    circle(screen, PURPLE, (pos[0] - round(112 * size), pos[1] - round(70 * size)), round(8 * size))
    circle(screen, BLACK, (pos[0] - round(115 * size), pos[1] - round(70 * size)), round(4 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(106 * size) - round(6 * size), pos[1] - round(75 * size),
                                       round(6 * size), round(4 * size)))

    ear1 = [pos[0] - round(96 * size), pos[1] - round(75 * size)]
    polygon(screen, WHITE, [ear1, (ear1[0] + round(15 * size), ear1[1] - round(22 * size)),
                            (ear1[0] - round(10 * size), ear1[1])])
    ear2 = [pos[0] - round(108 * size), pos[1] - round(80 * size)]
    polygon(screen, WHITE,
            [ear2, (ear2[0] + round(15 * size), ear2[1] - round(22 * size)), (ear2[0] - round(10 * size), ear2[1])])


def draw_flower(pos, size, num):
    '''
    Функция рисует цветы на кустах.
    pos - список из двух целочисленных значений, задающих координаты левого верхнего угла прямоугольника, в который
      вписывается центральный (желтый) эллипс в рисунке цветка
    size - вещественный параметр, служащий коэффициентом относительного размера
    num - целочисленный параметр, определяющий количество лепестков в цветках
    '''
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))

    if num == 9:
        param = [15, 7]
        param[0] = round(param[0] * size)
        param[1] = round(param[1] * size)
        flower_list = [ pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(10 * size), pos[1] + round(12 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(28 * size), pos[1] + round(5 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(25 * size), pos[1] + round(9 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(20 * size), pos[1] + round(13 * size), param[0], param[1])
                        ]
    elif num == 8:
        param = [15, 7]
        param[0] = round(param[0] * size)
        param[1] = round(param[1] * size)
        flower_list = [ pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(15 * size), pos[1] + round(12 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(25 * size), pos[1] + round(11 * size), param[0], param[1])
                        ]
    elif num == 7:
        param = [15.5, 7.5]
        param[0] = round(param[0] * size)
        param[1] = round(param[1] * size)
        flower_list = [ pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1])
                        ]
    elif num == 6:
        param = [17, 8]
        param[0] = round(param[0] * size)
        param[1] = round(param[1] * size)
        flower_list = [ pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(17 * size), pos[1] + round(1 * size), param[0], param[1]),
                        pygame.Rect(pos[0] + round(25 * size), pos[1] + round(6 * size), param[0], param[1])
                        ]

    for i in flower_list:
        ellipse(screen, random_color, i)
        ellipse(screen, BLACK, i, 1)

def bush(pos, size):
    '''
    Функция рисует куст.
    pos - список целочисленных значений, задающих координаты центра окружности, изображающей куст
    size - вещественный параметр, служащий коэффициентом относительного размера
    '''
    radius = 100
    circle(screen, L_GREEN, pos, round(radius * size))
    draw_flower_list = [
                       ((pos[0] - round(5 * size), pos[1] + round(35 * size)), 1.6 * size, randint(6, 9)),
                       ((pos[0] - round(70 * size), pos[1] - round(45 * size)), 1.4 * size, randint(6, 9)),
                       ((pos[0] - round(30 * size), pos[1] - round(20 * size)), 1.2 * size, randint(6, 9)),
                       ((pos[0] + round(10 * size), pos[1] - round(55 * size)), 1.8 * size, randint(6, 9)),
                       ((pos[0] - round(75 * size), pos[1] + round(25 * size)), 1.8 * size, randint(6, 9))
                       ]
    for i in draw_flower_list:
        draw_flower(*i)


pygame.init()

FPS = 30

# Размеры экрана
width = 900
height = 706

# Создание экрана и заливка его цветом
screen = pygame.display.set_mode((width, height))
screen.fill(SKY)

# Рисование ландшафта
mountains = [ (0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122), (490, 130), (570, 250),
              (750, 140), (900, 300), (900, 706), (0, 706)
              ]
grass = [ (0, 373), (38, 362), (75, 359), (114, 352), (271, 355), (280, 414), (294, 418), (900, 419), (900, 706),
        (0, 706)
          ]
landskape(mountains, grass)

# Рисование кустов
bush_list = [ ([420, 581], 0.7), ([650, 530], 0.5),  ([110, 625], 0.8), ([110, 625], 1.4), ([440, 400], 0.7),
            ([850, 450], 0.7)
              ]
for i in bush_list:
    bush(*i)

# Рисование лам
lama_list = [ ([500, 800], 0.7, True), ([600, 1000], 0.4, True), ([600, 800], 0.5), ([-80, 190], 3),
              ([600, 350], 1.5, True), ([800, 550], 0.7), ([900, 850], 0.7, True)
              ]
for i in lama_list:
    draw_lama(*i)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()