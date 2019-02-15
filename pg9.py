import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 600, 600
speed = [-2, 1]
bg = (255, 255, 255)
clock = pygame.time.Clock()
fullscreen = False
mode = pygame.display.list_modes()[0]
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption("初次见面，请多多关照！")

# 设置放大缩小的比例
ratio = 1.0

oturtle = pygame.image.load("turtle.png")
turtle = oturtle
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

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
                    width, height = mode
                else:
                    screen = pygame.display.set_mode(size)

            # 放大、缩小小乌龟(=\-)，空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 最大只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle, \
                                             (int(oturtle_rect.width * ratio), \
                                             int(oturtle_rect.height * ratio)))

                # 相应修改龟头两个朝向的 Surface 对象，否则一单击移动就打回原形 
                l_head = turtle
                r_head = pygame.transform.flip(turtle, True, False)
                # 获得小乌龟缩放后的新尺寸
                turtle_rect = turtle.get_rect()
            position.width, position.height = turtle_rect.width, turtle_rect.height
            
        # 用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)
                            
    # 移动图像
    position = position.move(speed)
    
    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()
    clock.tick(30)
