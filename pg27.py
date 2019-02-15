import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

xzq_sound = pygame.mixer.Sound("left.wav")
xzq_sound.set_volume(0.5)
xs_sound = pygame.mixer.Sound("right.wav")
xs_sound.set_volume(0.5)

bg_size = width, height = 640, 480
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Music")

pause = False

pause_image = pygame.image.load("pause.png").convert_alpha()
play_image = pygame.image.load("play.png").convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                xzq_sound.play()
            elif event.button == 3:
                xs_sound.play()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause

    screen.fill((255, 255, 255))

    if pause:
        screen.blit(pause_image, pause_rect)
        pygame.mixer.music.pause()
    else:
        screen.blit(play_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(30)
            


