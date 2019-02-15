import pygame
import sys
from pygame.locals import *
from random import *

# 球类继承自 Sprite 类
class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect_top = position
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)

def main():
    pygame.init()

    ball_image = "grey_ball.png"
    bg_image = "bg.png"

    running = True

    # 根据背景图片指定游戏界面尺寸
    bg_size = width, height = 640, 480
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball - FishC Demo")

    background = pygame.image.load(bg_image).convert_alpha()

    # 用来存放小球对象的列表
    balls = []

    # 创建 5 个小球
    for i in range(5):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, height - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed)
        balls.append(ball)

    clock = pygame.time.Clock()
        
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
        


