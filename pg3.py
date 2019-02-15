import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

f = open("record.txt", 'w')


while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')
        if event.type == pygame.QUIT:
            sys.exit()
        
