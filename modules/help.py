import pygame
from time import *
import io
import sys
sys.path.append('../')

pygame.init()
# Font type and size
font = pygame.font.Font('OCRAEXT.ttf', 50)
# Declares clock
clock = pygame.time.Clock()

# Color palette
BLUE_IO = ( 23,  53, 109)
OUTLINE = (252,  79,   0)
BLUE_F =  ( 23,  96, 109)
TEXT_M =  (255, 255, 255)

# Main background
BG = pygame.image.load('BG_Main.png').convert()

NAME = 'Help'
class helpbox:
    def __init__(self, text, rect):
        self.text = text
        self.box = pygame.Surface(rect[2:]).convert_alpha()
        self.pos = rect[:2]

    def draw(self):
        self.box.fill(pygame.Color(0, 0, 0, 0))
        text = font.render(self.text, True, TEXT_M)
        text_pos = [(self.box.get_size()[a] - text.get_size()[a])//2 for a in [0, 1]]
        self.box.blit(text, text_pos)

def setup():
    global box    
    box = helpbox("a label!", [60, 45, 360, 180])

def step(screen, events):
    global box

    screen.fill((0, 0, 0))
    screen.blit(BG, [0, 0])

    box.draw()
    screen.blit(box.box, box.pos)

    pygame.display.flip()

    clock.tick(30)