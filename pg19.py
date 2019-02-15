import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125) ]

size = width, height = 640, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.polygon(screen, GREEN, points, 0)

    pygame.display.flip()

    clock.tick(10)

