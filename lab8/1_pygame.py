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


def update_score(score):
    """
    Функция отвечает за отрисовку колличества очков, набранных игроком.
    """
    rect(screen, GREEN, (0, 0, 150, 40))
    my_font = pygame.font.Font(None, 50)
    score_string = "Счёт: " + str(score)
    if Target.point < 0:
        text_color = RED
    else:
        text_color = BLACK
    score_text = my_font.render(score_string, 1, text_color)
    screen.blit(score_text, (3, 3))


class Projectile:
    def __init__(self, x=40, y=450):
        """
        Конструктор класса Projectile
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
        self.live = 10
        self.dead = False

    def check_time(self):
        """
        Метод проверяет, не истекло ли время жизни мячика. Если истекло, то отключает его рисование.
        """
        self.live -= 0.03
        if self.live <= 0:
            self.x = self.y = self.x = 0
            self.dead = True

    def draw(self):
        """
        Метод реализует отрисовку мячика на экране.
        """
        if not self.dead:
            circle(screen, self.color, (round(self.x), round(self.y)), self.r)

    def move(self):
        """
        Метод отвечает за перемещение снаряда в пространстве и за проверку его соударения со стенами
        """
        if self.y <= 550:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
        elif self.vx ** 2 + self.vy ** 2 > 10:
            self.vy = -self.vy / 2
            self.vx = self.vx / 2
            self.y = 549
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779
        if self.x < 20:
            self.vx = -self.vx / 2
            self.x = 21
        self.draw()
        self.check_time()

    def hit_test(self, obj):
        """
        Метод проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r) ** 2 and not obj.cooldown():
            return True
        else:
            return False


class Gun:

    def __init__(self):
        """
        Инициализация объекта типа Gun.
        """
        self.power = 10
        self.on = False
        self.angle = 1
        self.x = 50
        self.y = 420

    def fire_start(self):
        """
        Метод отвечает за начало процесса заряжания
        """
        self.on = True

    def fire_end(self, projectile):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        new_projectile = Projectile()
        new_projectile.r += 5
        try:
            self.angle = math.atan((y - new_projectile.y) / (x - new_projectile.x))
        except ZeroDivisionError:
            self.angle = 2 * math.pi
        new_projectile.vx = self.power * math.cos(self.angle)
        new_projectile.vy = - self.power * math.sin(self.angle)
        projectile += [new_projectile]
        self.on = 0
        self.power = 10

    def targeting(self):
        """
        Прицеливание. Зависит от положения мыши.
        """
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        try:
            self.angle = math.atan((y - 450) / (x - 20))
        except ZeroDivisionError:
            self.angle = 2 * math.pi
        if self.on:
            line(screen, RED, (20, 450), (round(self.x), round(self.y)), 7)
        else:
            line(screen, BLACK, (20, 450), (round(self.x), round(self.y)), 7)
        self.x = 20 + max(self.power, 20) * math.cos(self.angle)
        self.y = 450 + max(self.power, 20) * math.sin(self.angle)
        self.power_up()


    def power_up(self):
        """
        Процесс набора "можности" выстрела.
        """
        if self.on:
            if self.power < 100:
                self.power += 1


class Target:
    point = 0

    def __init__(self, time=0):
        """
        Инициализация объектка класса Target.
        """
        self.color = choice(COLORS)
        self.r = rnd(2, 50)
        self.y = rnd(250, 450)
        self.x = rnd(550, 750)
        self.points = 0
        self.live = 1
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.time = time
        self.target_update()

    def move(self):
        """
        Метод отвечает за перемещение мишени.
        """
        self.x += self.vx
        self.y -= self.vy
        if self.y + self.r > 510 or self.y - self.r < 200:
            self.vy *= -1
        if self.x + self.r > 799 or self.x - self.r < 501:
            self.vx *= -1

    def target_update(self):
        """
        Метод прорисовывает мишень на экране.
        """
        if not self.cooldown():
            self.move()
            circle(screen, self.color, (self.x, self.y), self.r)
            circle(screen, BLACK, (self.x, self.y), self.r, 1)
        else:
            self.tick()

    def cooldown(self):
        """
        Фукция проверяет, находится ли появление мишени на перезарядке
        @return: логическое значение
        """
        if self.time > 100:
            return False
        else:
            return True

    def tick(self):
        """
        Метод отвечает за подсчёт времени до появления новой мишени
        """
        self.time += 1

    @staticmethod
    def hit(points=1):
        """
        Попадание снаряда в цель.
        """
        Target.point += points


g = Gun()
projectiles = []

clock = pygame.time.Clock()
finished = False
FPS = 30

targets = []
for i in range(2):
    t = Target(time=101)
    t.live = 1
    targets.append(t)


while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            g.fire_start()

        if event.type == pygame.MOUSEBUTTONUP:
            g.fire_end(projectiles)

        if event.type == pygame.QUIT:
            finished = True

    for projectile in projectiles:
        projectile.move()

    for t in targets:
        t.target_update()

        for b in projectiles:
            if b.hit_test(t):
                index = targets.index(t)
                t = Target()
                targets[index] = t
                t.hit()

    g.targeting()
    update_score(Target.point)
    pygame.display.update()

pygame.quit()
