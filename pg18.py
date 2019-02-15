import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width, height = 640, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10) # 边框向外扩展

    pygame.display.flip()

    clock.tick(10)

