import pygame
from time import *
import io
import sys
sys.path.append('../')
import home

NAME = 'INSERT MODULE NAME HERE'

def run(screen):
    pygame.init()
    # Font type and size
    font = pygame.font.Font('OCRAEXT.ttf', 9)
    # Declares clock
    clock = pygame.time.Clock()

    # Color palette
    BLUE_IO = ( 23,  53, 109)
    OUTLINE = (252,  79,   0)
    BLUE_F =  ( 23,  96, 109)
    TEXT_M =  (255, 255, 255)

    # Main background
    BG = pygame.image.load('BG_Main.png').convert()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                # Enter button
                if event.key == pygame.K_RETURN:
                    pass
                # Back button
                if event.key == pygame.K_BACKSPACE:
                    pass
        screen.fill((0, 0, 0))
        screen.blit(BG, [0, 0])

        """
        Screen contents go here
        """

        pygame.display.flip()

        clock.tick(30)
