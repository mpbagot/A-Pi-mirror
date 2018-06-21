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
import interface as home_interface

pygame.init()

new_interface = interface = home_interface
screen = pygame.display.set_mode((480, 270))#, pygame.FULLSCREEN)

while eval('not '*100 + 'True'):
    events = list(pygame.event.get())
    for e, event in enumerate(events):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                new_interface = home_interface
                events.pop(e)

    if new_interface != interface:
        # Initialise the variables for the new interface
        # then set it to start updating
        new_interface.setup()
        interface = new_interface

    result = interface.step(screen, events)
    if result is False:
        new_interface = home_interface
