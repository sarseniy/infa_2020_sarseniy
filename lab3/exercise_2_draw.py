import pygame
from pygame.draw import *

def flower(pos, size):
    ellipse(screen, YELLOW, pygame.Rect(pos[0] + 15 * size, pos[1] + 7 * size, 15 * size, 7 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 5 * size, pos[1] + 2 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 5 * size, pos[1] + 2 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 1 * size, pos[1] + 6 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 1 * size, pos[1] + 6 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 5 * size, pos[1] + 10 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 5 * size, pos[1] + 10 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 10 * size, pos[1] + 12 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 10 * size, pos[1] + 12 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 15 * size, pos[1] + 0 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 15 * size, pos[1] + 0 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 23 * size, pos[1] + 3 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 23 * size, pos[1] + 3 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 28 * size, pos[1] + 5 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 28 * size, pos[1] + 5 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 25 * size, pos[1] + 9 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 25 * size, pos[1] + 9 * size, 15 * size, 7 * size), 1)
    ellipse(screen, WHITE, pygame.Rect(pos[0] + 20 * size, pos[1] + 13 * size, 15 * size, 7 * size))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + 20 * size, pos[1] + 13 * size, 15 * size, 7 * size), 1)


def rotate(img, pos, angle):
    w, h = img.get_size()
    img2 = pygame.Surface((w*2, h*2), pygame.SRCALPHA)
    img2.blit(img, (w-pos[0], h-pos[1]))
    return pygame.transform.rotate(img2, angle)


RED = (255, 000, 000)
BLUE = (000, 000, 255)
GREEN = (000, 255, 000)
B_GREEN = (170, 222, 105)
L_GREEN = (112, 200, 55)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 000)
GRAY = (128, 128, 128)
BLACK = (000, 000, 000)
SKY = (185,211,238)
PURPLE = (229,128,255)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 706))

rect(screen, SKY, (0, 0, 500, 706))

polygon(screen, GRAY, [(0, 216), (60,73), (104,172), (172,93), (297,282), (389,88), (419,122), (500, 26), (500,706), (0,706)])
polygon(screen, BLACK, [(0, 216), (60,73), (104,172), (172,93), (297,282), (389,88), (419,122), (500, 26), (500,706), (0,706)], 1)

polygon(screen, B_GREEN, [(0,373), (38,362), (75,359), (114,352), (271,355), (280,414), (294,418), (500,419), (500,706), (0,706)])
polygon(screen, BLACK, [(0,373), (38,362), (75,359), (114,352), (271,355), (280,414), (294,418), (500,419), (500,706), (0,706)], 1)

ellipse(screen, WHITE, pygame.Rect(64, 445, 117, 46))
ellipse(screen, WHITE, pygame.Rect(151, 380, 34, 90))
ellipse(screen, WHITE, pygame.Rect(157, 362, 41, 25))
circle(screen, PURPLE, (176,375), 8)
circle(screen, BLACK, (179,375), 4)
ellipse(screen, WHITE, pygame.Rect(170, 370, 6, 4))
polygon(screen, WHITE, [(160,370), (145,348), (170,370)])
polygon(screen,WHITE, [(172, 370), (150, 340), (180, 365)])
ellipse(screen, WHITE, pygame.Rect(70, 462, 15, 40))
ellipse(screen, WHITE, pygame.Rect(70, 495, 15, 40))
ellipse(screen, WHITE, pygame.Rect(70, 530, 20, 11))

ellipse(screen, WHITE, pygame.Rect(95, 472, 15, 40))
ellipse(screen, WHITE, pygame.Rect(95, 505, 15, 40))
ellipse(screen, WHITE, pygame.Rect(95, 540, 20, 11))

ellipse(screen, WHITE, pygame.Rect(138, 462, 15, 40))
ellipse(screen, WHITE, pygame.Rect(138, 495, 15, 40))
ellipse(screen, WHITE, pygame.Rect(138, 530, 20, 11))

ellipse(screen, WHITE, pygame.Rect(156, 477, 15, 40))
ellipse(screen, WHITE, pygame.Rect(156, 510, 15, 40))
ellipse(screen, WHITE, pygame.Rect(156, 545, 20, 11))

circle(screen, L_GREEN, (420,581), 100)

flower((413,549), 1)
flower((430,570), 1)
flower((350,530), 1)
flower((380,510), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()