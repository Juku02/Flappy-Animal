import os,sys
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
    def clock_init():
        return pygame.time.Clock()
    
    @staticmethod
    def event_get():
        return pygame.event.get()
    
    @staticmethod
    def bg_image_load(image_path) -> pygame.Surface:
        return pygame.image.load(image_path)