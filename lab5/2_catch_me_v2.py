import datetime
import pygame
from pygame.draw import *
from pygame import mixer
from random import randint
from math import cos, pi, sin, radians
from os import path

pygame.mixer.init()
snd_dir = path.join(path.normpath(path.dirname(__file__)), 'sounds')
pop_sound1 = pygame.mixer.Sound(path.join(snd_dir, 'pop1.wav'))
pop_sound2 = pygame.mixer.Sound(path.join(snd_dir, 'pop2.wav'))
pop_sound3 = pygame.mixer.Sound(path.join(snd_dir, 'pop3.wav'))
SOUNDS = [pop_sound1, pop_sound2, pop_sound3]

pygame.init()

NUM = 3
MIN_R = 20
MAX_R = 100
WIDTH = 1200
HEIGHT = 600
FPS = 60
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


mixer.init()
music_dir = path.join(path.normpath(path.dirname(__file__)), 'sounds')
mixer.music.load(path.join(music_dir, 'background.mp3'))
mixer.music.set_volume(0.2)
mixer.music.play(loops=50)

count = 0
f1 = pygame.font.SysFont('serif', 150)
text2 = f1.render("Введите ваше имя", 0, (0, 180, 0))
screen.blit(text2, (10, 10))
pygame.display.update()
clock = pygame.time.Clock()

f = True
finished = False

string = ''
new_name = ''
while not finished:
    while f:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            if event.type == pygame.KEYDOWN:
                new_name = string
                if event.key == pygame.K_RETURN:
                    f = False
                    finished = True
                    break
                string += event.unicode
                f = pygame.font.SysFont('serif', 150)
                text = f.render(string, 0, (200, 0, 0))
                screen.blit(text, (10, 150))
                pygame.display.update()

screen.fill(BLACK)
pygame.display.update()

DATA = {'x': [], 'y': [], 'r': [], 'v': [], 'alpha': [], 'color': [], 'type': []}


def new_balls(num):
    """
    Функция рисует num мячиков.
    :param num: колличество мячиков
    """
    for k in range(num):
        DATA['x'].append(randint(MAX_R, WIDTH - MAX_R))
        DATA['y'].append(randint(MAX_R, HEIGHT - MAX_R))
        DATA['r'].append(randint(MIN_R, MAX_R))
        DATA['v'].append(randint(10, 500))
        DATA['v'][k] = float(DATA['v'][k])
        DATA['alpha'].append(randint(0, 360))
        DATA['alpha'][k] = radians(DATA['alpha'][k])
        DATA['color'].append(COLORS[randint(0, 5)])
        DATA['type'].append(TYPE[randint(0, 1)])
        if DATA['type'][k] == 'CIRCLE':
            circle(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k]), DATA['r'][k])
        if DATA['type'][k] == 'SQUARE':
            rect(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k], DATA['r'][k], DATA['r'][k]))


def move_balls():
    """
    Функция отвечает за передвижение мячиков по экрану.
    """
    for k in range(len(DATA['x'])):
        if DATA['type'][k] == 'CIRCLE':
            circle(screen, BLACK, (DATA['x'][k], DATA['y'][k]), DATA['r'][k])
        if DATA['type'][k] == 'SQUARE':
            rect(screen, BLACK, (DATA['x'][k], DATA['y'][k], DATA['r'][k], DATA['r'][k]))
        if DATA['type'][k] == 'CIRCLE':
            DATA['x'][k] += round(DATA['v'][k] / FPS * cos(DATA['alpha'][k]))
            DATA['y'][k] -= round(DATA['v'][k] / FPS * sin(DATA['alpha'][k]))
            circle(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k]), DATA['r'][k])
        if DATA['type'][k] == 'SQUARE':
            DATA['v'][k] *= randint(90, 110) / 100
            DATA['alpha'][k] += radians(randint(0, 10) - 5)
            DATA['x'][k] += round(DATA['v'][k] / FPS * cos(DATA['alpha'][k]))
            DATA['y'][k] -= round(DATA['v'][k] / FPS * sin(DATA['alpha'][k]))
            rect(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k], DATA['r'][k], DATA['r'][k]))
    check_walls()


def table(points):
    """
    Функция обеспечивает вывод в левый верхний угол экрана таблички с текущим счетом игрока.
    :param points: текущее колличество очков
    Функция подсмотрена у https://github.com/Ivan-Ivashkin
    """
    rect(screen, GREEN, (0, 0, 170, 40))
    my_font = pygame.font.Font(None, 50)
    score_string = "Счёт: " + str(points)
    if points < 0:
        text_color = RED
    else:
        text_color = BLACK
    score_text = my_font.render(score_string, 1, text_color)
    screen.blit(score_text, (3, 3))


def check_walls():
    """
    Функция проверяет удар мячика о стенку и считает новый угол
    """
    for k in range(len(DATA['x'])):
        if DATA['type'][k] == 'CIRCLE':
            if DATA['x'][k] + DATA['r'][k] > WIDTH - 10:
                DATA['alpha'][k] = radians(90 + randint(10, 170))
            if DATA['x'][k] - DATA['r'][k] < 0 + 10:
                DATA['alpha'][k] = radians(randint(10, 170) - 90)
            if DATA['y'][k] + DATA['r'][k] > HEIGHT - 10:
                DATA['alpha'][k] = radians(randint(10, 170))
            if DATA['y'][k] - DATA['r'][k] < 0 + 10:
                DATA['alpha'][k] = radians(randint(10, 170) - 180)
        if DATA['type'][k] == 'SQUARE':
            if DATA['x'][k] + DATA['r'][k] > WIDTH - 10:
                DATA['alpha'][k] = radians(90 + randint(10, 170))
            if DATA['x'][k] < 0 + 10:
                DATA['alpha'][k] = radians(randint(10, 170) - 90)
            if DATA['y'][k] + DATA['r'][k] > HEIGHT - 10:
                DATA['alpha'][k] = radians(randint(10, 170))
            if DATA['y'][k] < 0 + 10:
                DATA['alpha'][k] = radians(randint(10, 170) - 180)
        DATA['alpha'][k] %= 2 * pi


def respawn_figure(k):
    """
    Функция заново создаёт мишень после попадания в цель.
    :param k: номер "возрождаемого" элемента
    """
    DATA['x'][k] = randint(MAX_R, WIDTH - MAX_R)
    DATA['y'][k] = randint(MAX_R, HEIGHT - MAX_R)
    DATA['r'][k] = randint(MIN_R, MAX_R)
    DATA['v'][k] = randint(10, 500)
    DATA['alpha'][k] = randint(0, 360)
    DATA['alpha'][k] = radians(DATA['alpha'][k])
    DATA['color'][k] = COLORS[randint(0, 5)]
    DATA['type'][k] = TYPE[randint(0, 1)]
    if DATA['type'][k] == 'CIRCLE':
        circle(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k]), DATA['r'][k])
    if DATA['type'][k] == 'SQUARE':
        rect(screen, DATA['color'][k], (DATA['x'][k], DATA['y'][k], DATA['r'][k], DATA['r'][k]))


def check_click(action):
    """
    Функция проверяет, попал ли игрок по мячику, подсчитывает очки и рисует новые мячики при необходимости.
    :param action: параметры события
    """
    global count
    coord = action.pos
    for k in range(len(DATA['x'])):
        if DATA['type'][k] == 'CIRCLE':
            if (DATA['x'][k] - coord[0]) ** 2 + (DATA['y'][k] - coord[1]) ** 2 <= DATA['r'][k] ** 2:
                count += 1
                circle(screen, BLACK, (DATA['x'][k], DATA['y'][k]), DATA['r'][k])
                SOUNDS[randint(0, 2)].play()
                respawn_figure(k)
        if DATA['type'][k] == 'SQUARE':
            if 0 <= coord[0] - DATA['x'][k] <= DATA['r'][k] and 0 <= coord[1] - DATA['y'][k] <= DATA['r'][k]:
                count += 3
                rect(screen, BLACK, (DATA['x'][k], DATA['y'][k], DATA['r'][k], DATA['r'][k]))
                SOUNDS[randint(0, 2)].play()
                respawn_figure(k)


pygame.display.update()

finished = False


while not finished:
    clock.tick(FPS)
    new_balls(NUM)
    pygame.display.update()
    f = True
    while f:
        clock.tick(FPS)
        move_balls()
        table(count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event)
        pygame.display.update()

pygame.quit()

creating = open('records.txt', 'a', encoding='utf-8')
creating.close()

old_records = open('records.txt', 'r', encoding='utf-8')

names = []
results = []

for line in old_records:
    if line == '\n':
        break
    line.rstrip()
    name, result = line.split(' ')
    names.append(name)
    results.append(int(result))

old_records.close()

f = True
for i in range(len(names)):
    if names[i] == new_name:
        f = False
        if count > results[i]:
            results[i] = count

if f:
    names.append(new_name)
    results.append(count)

for i in range(len(names)):
    for j in range(i, len(names)):
        if results[j] > results[i]:
            results[i], results[j] = results[j], results[i]
            names[i], names[j] = names[j], names[i]

new_records = open('records.txt', 'w', encoding='utf-8')

for i in range(len(names)):
    print(names[i], results[i], file=new_records)
print('\n', file=new_records)

today = datetime.datetime.today()
print('Last updated:', today.strftime("%Y-%m-%d-%H:%M:%S MSK"), file=new_records)

new_records.close()
