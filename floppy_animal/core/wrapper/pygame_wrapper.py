import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
from floppy_animal.core.utils import Any

class PyGameWrapper:
    @staticmethod
    def init() -> None:
        pygame.init()
        
    @staticmethod
    def close() -> None:
        pygame.quit()
        
    @staticmethod
    def display_set_mode(width, heigth):
        return pygame.display.set_mode([width,heigth])
    
    @staticmethod
    def display_flip() -> None:
        pygame.display.flip()
    
    @staticmethod
    def event_handler() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            else:
                return True
            
    @staticmethod
    def clock_init() -> Any:
        return pygame.time.Clock()