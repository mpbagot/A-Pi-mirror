import pygame
import math
from time import *
import io
import sys, os
sys.path.append('../')

CHANNEL = pygame.mixer.Channel(0)

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
    global selection
    global volume
    volume = 0
    scroll = 0
    selection = [0]
    mboxes = []
    songs = []
    path = "modules/music_data"
    direc = os.listdir(path)
    for file in direc:
        if file.split('.')[-1] in ['wav', 'ogg']:
            songs.append(file)

    for s in range(len(songs)):
        #
        box = Mbox(songs[s], [0, s*20, 50, 20])
        #
        box.file = pygame.mixer.Sound('{}/{}'.format(path, songs[s]))
        mboxes.append(box)


def step(screen, events):
    global scroll
    global mboxes
    global selection
    global volume

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selection[0] -= 1
                selection[0] %= len(mboxes)

            if event.key == pygame.K_DOWN:
                selection[0] += 1
                selection[0] %= len(mboxes)

            if event.key == pygame.K_LEFT:
                volume += 0.05

            if event.key == pygame.K_RIGHT:
                volume -= 0.05

            # Enter button
            if event.key == pygame.K_RETURN:
                pass

            # Back button
            if event.key == pygame.K_BACKSPACE:
                pass

    if volume < 0:
        volume = 0
    if volume > 1:
        volume = 1


    screen.fill((0, 0, 0))
    screen.blit(BG, [0, 0])
    for y, box in enumerate(mboxes):
        Mbox.update(scroll)
        Mbox.draw([y] == selection)
        screen.blit(mbox.box, mbox.pos)

    screen.blit(OV, [0, 0])
    pygame.display.flip()

    clock.tick(30)
