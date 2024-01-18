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
    FLAP_BUTTON = pygame.USEREVENT + 2

class Event_type(Enum):
    QUIT = 0,
    MOUSE_CLICK = 1,
    WINDOW_RESIZE = 2,
    CHANGE_SCENE = 3,
    LEFT_MOUSE_CLICK = 4

class Character_sprite(Enum):
    PIGEON = 1,
    CHICK = 2,
    SHARK = 3,

class Player_mode(Enum):
    SHM = "SHM"
    NORMAL = "NORMAL"
    CRASH = "CRASH"
