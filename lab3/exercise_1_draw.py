import pygame
from pygame.draw import *

RED = (255, 000, 000)
BLUE = (000, 000, 255)
GREEN = (000, 255, 000)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 000)
GRAY = (128, 128, 128)
BLACK = (000, 000, 000)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, WHITE, (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 1)

rect(screen, BLACK, (150, 240, 100, 20))

circle(screen, RED, (150, 180), 25)
circle(screen, BLACK, (150, 180), 25, 1)
circle(screen, BLACK, (150, 180), 10)

circle(screen, RED, (250, 180), 20)
circle(screen, BLACK, (250, 180), 20, 1)
circle(screen, BLACK, (250, 180), 10)

polygon(screen, BLACK, [(175, 170), (185, 160), (105, 100), (95, 110)])

polygon(screen, BLACK, [(225, 160), (228, 170), (290, 140), (287, 130)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
