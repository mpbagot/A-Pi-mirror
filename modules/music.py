import pygame
import math
from time import *
import io
import sys

NAME = 'Music'

def run(screen):

    # Font type and size
    font = pygame.font.Font('OCRAEXT.ttf', 18)
    # Declares clock
    clock = pygame.time.Clock()
    
    class Mboxes:
        def __init__(self, text, rect):
            self.text = text
            self.box = pygame.Surface(rect[2:])
            self.pos = rect[:2]
            self.default_pos = rect[:2]
            self.file = None

        def draw(self, selected):
            if selected:
                self.box.fill(BLUE_F)

                text = font.render(self.text, True, TEXT_M)
                text_pos = [(self.box.get_size()[a] - text.get_size()[a])//2 for a in [0, 1]]
                self.box.blit(text, text_pos)

                # Border
                pygame.draw.rect(self.box, OUTLINE, self.box.get_rect(), 3)
            else:
                self.box.fill(BLUE_F)

                text = font.render(self.text, True, TEXT_M)
                text_pos = [(self.box.get_size()[a] - text.get_size()[a])//2 for a in [0, 1]]
                self.box.blit(text, text_pos)

                # Border
                pygame.draw.rect(self.box, BLUE_IO, self.box.get_rect(), 3)



        def update(self, scroll):
            self.pos[0] = self.default_pos[0] + scroll




    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
