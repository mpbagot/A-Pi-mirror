import hashlib
import socket

## Figure out if this is the correct device or not
is_rpi = '6de8718a0787872457dba333cba3b836ae01801c39b65aed6e2f7982d5f08526' == hashlib.sha256(socket.gethostname().encode()).hexdigest()
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
