import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 600, 600
bg = (255, 255, 255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")
turtle = pygame.image.load("turtle.png")
position = turtle_rect = turtle.get_rect()
# 小乌龟顺时针行走
speed = [5, 0]
turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle
# 刚开始走顶部
turtle = turtle_top

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                                        
    position = position.move(speed)
    if position.right > width:
        turtle = turtle_right
        # 变换后矩形的尺寸发生改变
        position = turtle_rect = turtle.get_rect()
        # 矩形尺寸的改变导致位置也有变化
        position.left = width - turtle_rect.width
        speed = [0, 5]
    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5, 0]
    if position.left == 0:
        turtle = turtle_left
        positon = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        print(position.left)
        speed = [1, -5]
    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()
    clock.tick(30)
