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

figures = []


def new_balls(num):
    """
    Функция рисует num мячиков.
    :param num: колличество мячиков
    """
    for k in range(num):
        x = randint(MAX_R, WIDTH - MAX_R)
        y = randint(MAX_R, HEIGHT - MAX_R)
        r = randint(MIN_R, MAX_R)
        v = randint(10, 500)
        v = float(v)
        alpha = randint(0, 360)
        alpha = radians(alpha)
        color = COLORS[randint(0, 5)]
        fig_type = TYPE[randint(0, 1)]
        figure = {'x': x, 'y': y, 'r': r, 'v': v, 'alpha': alpha, 'color': color, 'fig_type': fig_type}
        figures.append(figure)
        if fig_type == 'CIRCLE':
            circle(screen, color, (x, y), r)
        if fig_type == 'SQUARE':
            rect(screen, color, (x, y, r, r))


def move_balls():
    """
    Функция отвечает за передвижение мячиков по экрану.
    """
    for fig in figures:
        if fig['fig_type'] == 'CIRCLE':
            circle(screen, BLACK, (fig['x'], fig['y']), fig['r'])
        if fig['fig_type'] == 'SQUARE':
            rect(screen, BLACK, (fig['x'], fig['y'], fig['r'], fig['r']))
        if fig['fig_type'] == 'CIRCLE':
            fig['x'] += round(fig['v'] / FPS * cos(fig['alpha']))
            fig['y'] -= round(fig['v'] / FPS * sin(fig['alpha']))
            circle(screen, fig['color'], (fig['x'], fig['y']), fig['r'])
        if fig['fig_type'] == 'SQUARE':
            fig['v'] *= randint(90, 110) / 100
            fig['alpha'] += radians(randint(0, 10) - 5)
            fig['x'] += round(fig['v'] / FPS * cos(fig['alpha']))
            fig['y'] -= round(fig['v'] / FPS * sin(fig['alpha']))
            rect(screen, fig['color'], (fig['x'], fig['y'], fig['r'], fig['r']))
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
    for fig in figures:
        if fig['fig_type'] == 'CIRCLE':
            if fig['x'] + fig['r'] > WIDTH - 10:
                fig['alpha'] = radians(90 + randint(10, 170))
            if fig['x'] - fig['r'] < 0 + 10:
                fig['alpha'] = radians(randint(10, 170) - 90)
            if fig['y'] + fig['r'] > HEIGHT - 10:
                fig['alpha'] = radians(randint(10, 170))
            if fig['y'] - fig['r'] < 0 + 10:
                fig['alpha'] = radians(randint(10, 170) - 180)
        if fig['fig_type'] == 'SQUARE':
            if fig['x'] + fig['r'] > WIDTH - 10:
                fig['alpha'] = radians(90 + randint(10, 170))
            if fig['x'] < 0 + 10:
                fig['alpha'] = radians(randint(10, 170) - 90)
            if fig['y'] + fig['r'] > HEIGHT - 10:
                fig['alpha'] = radians(randint(10, 170))
            if fig['y'] < 0 + 10:
                fig['alpha'] = radians(randint(10, 170) - 180)
        fig['alpha'] %= 2 * pi


def respawn_figure(k):
    """
    Функция заново создаёт мишень после попадания в цель.
    :param k: номер "возрождаемого" элемента
    """
    fig = figures[k]
    fig['x'] = randint(MAX_R, WIDTH - MAX_R)
    fig['y'] = randint(MAX_R, HEIGHT - MAX_R)
    fig['r'] = randint(MIN_R, MAX_R)
    fig['v'] = randint(10, 500)
    fig['alpha'] = randint(0, 360)
    fig['alpha'] = radians(fig['alpha'])
    fig['color'] = COLORS[randint(0, 5)]
    fig['fig_type'] = TYPE[randint(0, 1)]
    if fig['fig_type'] == 'CIRCLE':
        circle(screen, fig['color'], (fig['x'], fig['y']), fig['r'])
    if fig['fig_type'] == 'SQUARE':
        rect(screen, fig['color'], (fig['x'], fig['y'], fig['r'], fig['r']))


def check_click(action):
    """
    Функция проверяет, попал ли игрок по мячику, подсчитывает очки и рисует новые мячики при необходимости.
    :param action: параметры события
    """
    global count
    coord = action.pos
    for fig in figures:
        if fig['fig_type'] == 'CIRCLE':
            if (fig['x'] - coord[0]) ** 2 + (fig['y'] - coord[1]) ** 2 <= fig['r'] ** 2:
                count += 1
                circle(screen, BLACK, (fig['x'], fig['y']), fig['r'])
                SOUNDS[randint(0, 2)].play()
                respawn_figure(figures.index(fig))
        if fig['fig_type'] == 'SQUARE':
            if 0 <= coord[0] - fig['x'] <= fig['r'] and 0 <= coord[1] - fig['y'] <= fig['r']:
                count += 3
                rect(screen, BLACK, (fig['x'], fig['y'], fig['r'], fig['r']))
                SOUNDS[randint(0, 2)].play()
                respawn_figure(figures.index(fig))


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
