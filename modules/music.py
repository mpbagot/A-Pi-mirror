import pygame
import math
from time import *
import io
import sys, os

try:
    import mutagen.oggvorbis
except:
    print('[WARNING] Mutagen not found. Some features are not supported.')
    mutagen = None

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
        self.pos[1] = self.default_pos[1] + scroll

pygame.init()
# Font type and size
font = pygame.font.Font('resources/font/ocraext.ttf', 9)
font1 = pygame.font.Font('resources/font/ocraext.ttf', 20)

# Declares clock
clock = pygame.time.Clock()
#Color palette
BLUE_IO = ( 23,  53, 109)
OUTLINE = (252,  79,   0)
BLUE_F =  ( 23,  96, 109)
TEXT_M =  (255, 255, 255)
BG = pygame.image.load('resources/textures/bg_main.png').convert()
OV = pygame.image.load('modules/Overlays/Musicalpha.png').convert_alpha()


NAME = 'Music'

def setup():
    global mboxes
    global selection
    global volume
    global buff_song
    global text_p
    global playing
    global paused

    text_p = [(20,100),(20,200)]
    volume = 0.5
    selection = 0
    playing = 0
    paused = False
    mboxes = []
    songs = []
    path = "modules/music_data"
    direc = os.listdir(path)
    for file in direc:
        if file.split('.')[-1] in ['wav', 'ogg']:
            songs.append(file)

    for s in range(len(songs)):
        #
        label = '.'.join(songs[s].split('.')[:-1])
        box = Mbox(label, [185, 105 + (s - selection) * 30, 285, 30])
        #
        box.file = '{}/{}'.format(path, songs[s])
        mboxes.append(box)

    buff_song = None

def step(screen, events):
    global mboxes
    global selection
    global volume
    global buff_song
    global text_p
    global playing
    global paused

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selection -= 1
                selection = max(0, selection)

            if event.key == pygame.K_DOWN:
                selection += 1
                selection = min(len(mboxes)-1, selection)

            if event.key == pygame.K_LEFT:
                volume -= 0.05

            if event.key == pygame.K_RIGHT:
                volume += 0.05

            # Enter button
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.load(mboxes[selection].file)
                playing = selection
                buff_song = pygame.mixer.Sound(mboxes[selection].file)
                pygame.mixer.music.play()

            # Back button
            if event.key == pygame.K_BACKSPACE:
                if not paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                paused = not paused

    if volume < 0:
        volume = 0
    if volume > 1:
        volume = 1
    pygame.mixer.music.set_volume(volume)

    screen.fill((0, 0, 0))
    screen.blit(BG, [0, 0])
    for y, box in enumerate(mboxes):
        box.update(selection * -30)
        if 14 < box.pos[1] < 215:
            box.draw(y == selection)
            screen.blit(box.box, box.pos)

    screen.blit(OV, [0, 0])

    # Get the tags
    if buff_song:
        filename = mboxes[playing].file
        if mutagen:
            if filename.endswith('.ogg'):
                ogg_file = mutagen.oggvorbis.OggVorbis(filename)
                tags = {a[0] : a[1] for a in ogg_file.tags}
            elif filename.endswith('.wav'):
                tags = {'TITLE' : filename}

        else:
            tags = {'TITLE' : filename}

        length = round(buff_song.get_length(), 1)
        play_time = round(pygame.mixer.music.get_pos()/1000, 1)

        # Draw the tags
        # Title, artist, current time out of total time
        # TITLE for title
        # ARTIST for artist
        # play_time is the number of seconds that it has been playing
        # length is the number of seconds the song goes for
        # 0 = 20, 300
        # 1 = 20, 200
        play_info = (str(play_time) + ' / ' + str(length))
        p_txt = font1.render(play_info, True, TEXT_M)
        screen.blit(p_txt, text_p[1])

    clock.tick(30)
