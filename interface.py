NAME = 'main'
from time import *
import pygame
import math
import io
import sys
import importlib

class Box:
    def __init__(self, text, rect):#x, y, w, h):
        self.text = text
        self.box = pygame.Surface(rect[2:])
        self.pos = rect[:2]
        self.default_pos = rect[:2]
        self.module = None

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
font = pygame.font.Font('OCRAEXT.ttf', 18)
# Declares clock
clock = pygame.time.Clock()

#Color palette
BLUE_IO = ( 23,  53, 109)
OUTLINE = (252,  79,   0)
BLUE_F =  ( 23,  96, 109)
TEXT_M =  (255, 255, 255)

BG = pygame.image.load('BG_Main.png').convert()

def setup():
    global boxes
    global selection
    global scroll_amount

    scroll_amount = 0

    # Selection is [x, y]
    selection = [0, 0]

    programs = []
    for line in open('modules/programs.txt'):
        line = line.strip()
        try:
            module = importlib.import_module("modules."+line)
            print(module)
            programs.append((module.NAME, module))
        except ImportError:
            print(line, 'failed to import')

    boxes = []
    programs.sort()
    for p in range(0, len(programs), 2):
        column = []
        box = Box(programs[p][0], [70+p//2*190, 55, 150, 70])
        box.module = programs[p][1]
        column.append(box)
        if p+1 < len(programs):
            box = Box(programs[p+1][0], [70+p//2*190, 145, 150, 70])
            box.module = programs[p+1][1]
            column.append(box)
        boxes.append(column)


def step(screen, events):
    global boxes
    global selection
    global scroll_amount
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selection[1] -= 1
                selection[1] %= 2
            if event.key == pygame.K_DOWN:
                selection[1] += 1
                selection[1] %= 2
            if event.key == pygame.K_LEFT:
                selection[0] -= 1
                selection[0] %= len(boxes)
            if event.key == pygame.K_RIGHT:
                selection[0] += 1
                selection[0] %= len(boxes)
            if event.key == pygame.K_RETURN:
                # print('meh')
                return boxes[selection[0]][selection[1]].module

            if len(boxes[selection[0]]) == 1 and selection[1]:
                selection[1] = 0


    screen.fill((0, 0, 0))
        # if box.pos[0] > 190*(len(column)):
        #     box.pos[0] = 190*(len(column))

    if scroll_amount > 0:
        scroll_amount = 0
    screen.blit(BG, [0, 0])
        # Draw boxes
    scroll_amount = -190 * selection[0]
    for x, column in enumerate(boxes):
        for y, box in enumerate(column):
            box.update(scroll_amount)
            box.draw([x, y] == selection)
            screen.blit(box.box, box.pos)

    pygame.display.flip()

    clock.tick(30)
    return True
