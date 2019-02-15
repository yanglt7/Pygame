import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 500, 300
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FichC Demo")

turtle = pygame.image.load("turtle1.png").convert_alpha()
background = pygame.image.load("background.jpg").convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

for i in range(position.width):
    for j in range(position.height):
        temp = turtle.get_at((i, j))
        if temp[3] != 0:
            temp[3] = 200
        turtle.set_at((i, j), temp)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, (0, 0))
    screen.blit(turtle, position)

    pygame.display.flip()
    
    clock.tick(30)
