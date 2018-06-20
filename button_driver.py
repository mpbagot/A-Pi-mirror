# Import Raspberry Pi GPIO module
import RPi.GPIO as GPIO
import pygame

GPIO.setmode(GPIO.BCM)

# Define the pin numbers
UP_PIN = 10
DOWN_PIN = 9
LEFT_PIN = 11
RIGHT_PIN = 0
HOME_PIN = 8
BACK_PIN = 7
ENTER_PIN = 1

# Define the keybind numbers for the Pygame event
B_UP = pygame.K_UP
B_DOWN = pygame.K_DOWN
B_LEFT = pygame.K_LEFT
B_RIGHT = pygame.K_RIGHT
B_HOME = pygame.K_h
B_BACK = pygame.K_b
B_ENTER = pygame.K_RETURN

# Create a binding between the two
buttons = {
            UP_PIN : B_UP,
            DOWN_PIN : B_DOWN,
            LEFT_PIN : B_LEFT,
            RIGHT_PIN : B_RIGHT,
            HOME_PIN : B_HOME,
            BACK_PIN : B_BACK,
            ENTER_PIN : B_ENTER
          }

def fire_keydown(pin):
    '''
    Fire a Pygame event corresponding to the GPIO signal
    '''
    event = pygame.event.Event(pygame.KEYDOWN, key=buttons.get(pin))
    pygame.event.post(event)

def shutdown():
    '''
    Clean up the GPIO data before shutting down
    '''
    GPIO.cleanup()

# Setup the pull-up resistors and add event hooks to fire pygame events
for pin_id in buttons:
    GPIO.setup(pin_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin_id, GPIO.RISING, callback=fire_keydown, bouncetime=100)
