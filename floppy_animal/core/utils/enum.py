from enum import Enum
import pygame

class Even_value(Enum):
    QUIT = pygame.QUIT,
    MOUSE_CLICK = pygame.MOUSEBUTTONUP,
    K_DOWN = pygame.K_UP,
    K_UP = pygame.K_DOWN,
    K_LEFT = pygame.K_LEFT,
    K_RIGHT = pygame.K_RIGHT,

class Event_type(Enum):
    QUIT = 0,
    MOUSE_CLICK = 1,
