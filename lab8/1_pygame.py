from random import randrange as rnd, choice
import math
import pygame
from pygame.draw import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
pygame.display.update()


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
        self.id = circle(screen, self.color, (self.x, self.y), self.r)
        self.live = 10

    def check_time(self):
        self.live -= 0.03
        if self.live <= 0:
            self.color = WHITE

    def set_coords(self):
        circle(screen, self.color, (round(self.x), round(self.y)), self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if 600 > self.y + self.r > 560:
            dvy = 0
        else:
            dvy = 2
        self.y -= self.vy
        self.x += self.vx
        self.vy -= dvy
        self.set_coords()
        if self.y + self.r > 560:
            self.vy *= -1
        if (self.x + self.r > 780) or (self.x - self.r < 20):
            self.vx *= -1
        if self.y + self.r > 559:
            self.vy /= 1.3
            self.vx /= 1.3
        self.check_time()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r) ** 2:
            return True
        else:
            return False


class Gun:

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 50
        self.y = 420
        line(screen, BLACK, (20, 450), (self.x, self.y), 7)

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, balls, bullet):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((y - new_ball.y) / (x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        self.an = math.atan((y - 450) / (x - 20))
        if self.f2_on:
            line(screen, RED, (20, 450), (self.x, self.y), 7)
        else:
            line(screen, BLACK, (20, 450), (self.x, self.y), 7)
        self.x = 20 + max(self.f2_power, 20) * math.cos(self.an)
        self.y = 450 + max(self.f2_power, 20) * math.sin(self.an)
        self.power_up()


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1


def update_score():
    rect(screen, GREEN, (0, 0, 130, 40))
    my_font = pygame.font.Font(None, 50)
    score_string = "Счёт: " + str(Target.point)
    if Target.point < 0:
        text_color = RED
    else:
        text_color = BLACK
    score_text = my_font.render(score_string, 1, text_color)
    screen.blit(score_text, (3, 3))


class Target:
    point = 0

    def __init__(self):
        self.color = choice(COLORS)
        self.r = rnd(2, 50)
        self.y = rnd(300, 550)
        self.x = rnd(600, 780)
        self.points = 0
        self.live = 1
        self.target_update()

    def target_update(self):
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, BLACK, (self.x, self.y), self.r, 1)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        Target.point += points


g1 = Gun()
bullet = 0
balls = []

clock = pygame.time.Clock()
finished = False
FPS = 30

targets = []
for t in range(2):
    t = Target()
    t.live = 1
    targets.append(t)


while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            g1.fire2_start()
        if event.type == pygame.MOUSEBUTTONUP:
            g1.fire2_end(balls, bullet)
        if event.type == pygame.QUIT:
            finished = True
    for ball in balls:
        ball.move()
    for t in targets:
        t.target_update()
        for b in balls:
            if b.hittest(t):
                index = targets.index(t)
                t = Target()
                targets[index] = t
                t.hit()
    print(Target.point)
    g1.targetting()
    update_score()
    pygame.display.update()
