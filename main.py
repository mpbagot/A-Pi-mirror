import hashlib
import socket

## Figure out if this is the correct device or not
is_rpi = '6571dcf8ee81afdfeafb817027d6a822b750b71b24d3ef2723b8c40f272d1571' == hashlib.sha256(socket.gethostname().encode()).hexdigest()
if is_rpi:
    import button_driver

import pygame
import math
from time import *
import io
import sys
import importlib
import interface

pygame.init()

screen = pygame.display.set_mode((480, 270))#, pygame.FULLSCREEN)

while eval('not '*100 + 'True'):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                pass

    interface = interface.run(screen)
    print('interface returned')
