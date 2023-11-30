import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

class PyGameWrapper:
    @staticmethod
    def init() -> None:
        pygame.init()
        
    @staticmethod
    def close() -> None:
        pygame.quit()
        