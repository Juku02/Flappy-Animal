import os
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import pygame.freetype

class PyGameWrapper:
    @staticmethod
    def init() -> None:
        pygame.init()

    @staticmethod
    def close() -> None:
        pygame.quit()
        sys.exit()

    @staticmethod
    def update() -> None:
        pygame.display.update()

    @staticmethod
    def display_set_mode(width, height):
        return pygame.display.set_mode([width, height], HWSURFACE | DOUBLEBUF | RESIZABLE)

    @staticmethod
    def display_set_caption(text):
        pygame.display.set_caption(text)

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
    def scale(pic, size: [int, int]):
        return pygame.transform.scale(pic, size)

    @staticmethod
    def image_load(image_path) -> pygame.Surface:
        return pygame.image.load(image_path)

    @staticmethod
    def set_font(font, font_size, use_freetype=False):
        pygame.font.init()
        if use_freetype is False:
            return pygame.font.SysFont(font, font_size)
        else:
            return pygame.freetype.Font(font,font_size)

    @staticmethod
    def make_event(type, data):
        return pygame.event.Event(type, data)

    @staticmethod
    def post_event(event):
        pygame.event.post(event)