import os,sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import pygame.freetype 
from floppy_animal.core.utils import Any

class PyGameWrapper:
    @staticmethod
    def init() -> None:
        pygame.init()
         
    @staticmethod
    def close() -> None:
        pygame.quit()
    
    @staticmethod 
    def update() -> None:
        pygame.display.update()
        
    @staticmethod
    def display_set_mode(width, heigth):
        return pygame.display.set_mode([width,heigth],pygame.RESIZABLE)    
    
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
    
    @staticmethod
    def set_font(font, font_size, use_freetype=False):
        pygame.font.init()
        if use_freetype is False:
            return pygame.font.SysFont(font, font_size)
        else:
            return pygame.freetype.Font(font,font_size)