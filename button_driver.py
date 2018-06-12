# Import Raspberry Pi GPIO module
import RPi.GPIO as GPIO
import pygame

# Define the pin numbers
UP_PIN = None
DOWN_PIN = None
LEFT_PIN = None
RIGHT_PIN = None
HOME_PIN = None
BACK_PIN = None
ENTER_PIN = None

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

# Add event hooks to fire pygame events
GPIO.add_event_detect(UP_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
GPIO.add_event_detect(DOWN_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
GPIO.add_event_detect(LEFT_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
GPIO.add_event_detect(RIGHT_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)

GPIO.add_event_detect(HOME_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
GPIO.add_event_detect(BACK_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
GPIO.add_event_detect(ENTER_PIN, GPIO.RISING, callback=fire_keydown, bouncetime=100)
