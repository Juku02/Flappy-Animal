from enum import Enum
import pygame

class Event_value(Enum):
    QUIT = pygame.QUIT,
    MOUSE_CLICK = pygame.MOUSEBUTTONUP,
    WINDOW_RESIZE = pygame.VIDEORESIZE
    K_DOWN = pygame.K_UP,
    K_UP = pygame.K_DOWN,
    K_LEFT = pygame.K_LEFT,
    K_RIGHT = pygame.K_RIGHT,
    CHANGE_SCENE = pygame.USEREVENT + 1

class Event_type(Enum):
    QUIT = 0,
    MOUSE_CLICK = 1,
    WINDOW_RESIZE = 2,
    CHANGE_SCENE = 3,
