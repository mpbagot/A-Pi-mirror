import hashlib
import socket

## Figure out if this is the correct device or not
is_rpi = '101c18234e9c936f8069b8de1a9e959ad0ba4af19a0cc8adb3f4c62f8de8ff1a' == hashlib.sha256(socket.gethostname().encode()).hexdigest()
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

    interface = interface.run(screen)
