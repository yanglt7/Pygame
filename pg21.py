import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)

size = width, height = 640, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")

position = size[0] // 2, size[1] // 2
moving = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill(WHITE)

    pygame.draw.ellipse(screen, BLACK, (100, 100, 440, 100), 1)
    pygame.draw.ellipse(screen, BLACK, (220, 50, 200, 200), 1)
    
    pygame.display.flip()

    clock.tick(120)

