import pygame
import sys
from pygame.locals import *

# 初始化Pygame
pygame.init()

size = width, height = 600, 600
width1 = width
height1 = height
speed = [-2, 1]
bg = (255, 255, 255)

fullscreen = False

mode = pygame.display.list_modes()[0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")
turtle = pygame.image.load("turtle.png")
position = turtle.get_rect()

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed == [0, 1]

            # 全屏(F11)
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((mode), FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
                                        

    # 移动图像
    position = position.move(speed)

    if event.type == KEYDOWN:
        if event.key == K_F11:
            width1 = mode[1]
            height1 = mode[0]       
        
    if position.left < 0 or position.right > width1:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height1:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟25毫秒
    pygame.time.delay(25)
