#!/usr/bin/env python3
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

pygame.init()

display = pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)
screen = pygame.Surface((480, 270))

pygame.mouse.set_visible(False)

import interface as home_interface
new_interface = home_interface
interface = None

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
    # Rescale the smaller surface to the actual screen size
    display.blit(pygame.transform.scale(screen, display.get_size()), [0, 0])
    pygame.display.flip()

    supports_api = all([a in dir(result) for a in ['setup', 'step']])
    if result is False:
        new_interface = home_interface
    elif result.__class__.__name__ == 'module':
        if supports_api:
            new_interface = result
        else:
            print('[ERROR] Module doesn\'t implement program API correctly.')
