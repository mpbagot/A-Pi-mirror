import pygame
from time import *
import io
import sys
sys.path.append('../')

pygame.init()
# Font type and size
font = pygame.font.Font('OCRAEXT.ttf', 10)
# Declares clock
clock = pygame.time.Clock()

# Color palette
BLUE_IO = ( 23,  53, 109)
OUTLINE = (252,  79,   0)
BLUE_F =  ( 23,  96, 109)
TEXT_M =  (255, 255, 255)

# Main background
BG = pygame.image.load('BG_Main.png').convert()
txt = "Welcome to the A-Pi \n This system comes standard with a music player module. \n The music player supports only \'WAV\' and/or \'OGG\' formats. \n To use the music player, up/down directional keys change selection. \n Left/right directional keys change volume and backspace plays/pauses. \n To return home use the \'h\' key \n NOTE keys cannot be held down for continuous input."
NAME = 'Help'
class helpbox:
    def __init__(self, text, rect):
        self.text = text
        self.box = pygame.Surface(rect[2:]).convert_alpha()
        self.pos = rect[:2]

    def draw(self):
        self.box.fill(pygame.Color(0, 0, 0, 0))
        for l, line in enumerate(self.text.split('\n')):
            text = font.render(line, True, TEXT_M)
            text_pos = [(self.box.get_width() - text.get_width())//2, 10 + 12 * l]
            self.box.blit(text, text_pos)

def setup():
    global box
    box = helpbox(txt, [60, 45, 360, 180])

def step(screen, events):
    global box

    screen.fill((0, 0, 0))
    screen.blit(BG, [0, 0])

    box.draw()
    screen.blit(box.box, box.pos)

    clock.tick(30)
