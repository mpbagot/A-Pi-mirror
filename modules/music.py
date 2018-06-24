import pygame
import math
from time import *
import io
import sys, os
sys.path.append('../')

class Mbox:
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

pygame.init()
# Font type and size
font = pygame.font.Font('OCRAEXT.ttf', 9)
# Declares clock
clock = pygame.time.Clock()
#Color palette
BLUE_IO = ( 23,  53, 109)
OUTLINE = (252,  79,   0)
BLUE_F =  ( 23,  96, 109)
TEXT_M =  (255, 255, 255)
BG = pygame.image.load('BG_Main.png').convert()
OV = pygame.image.load('modules/overlays/Musicalpha.png').convert_alpha()


NAME = 'Music'

def setup():
    global scroll
    global mboxes
    global s_selection
    global volume
    volume = 0
    scroll = 0
    selection = [0]
    mboxes = []
    songs = []
    path = "modules/music_data"
    direc = os.listdir(path)
    for file in direc:
        songs.append(file)


def step(screen, events):
    global scroll
    global mboxes
    global s_selection
    global volume

    for event in events:
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
    for y, box in enumerate(row):
        mbox.update(scroll_amount)
        mbox.draw([y] == selection)
        screen.blit(mbox.box, mbox.pos)

    screen.blit(OV, [0, 0])
    pygame.display.flip()

    clock.tick(30)
