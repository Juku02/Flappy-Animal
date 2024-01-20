from flappy_animal.core.commons import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from flappy_animal.core.utils import Union, Tuple, List, Any
import pygame as pygame
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
    def display_set_mode(width: Union[int,float], height: Union[int,float]) -> Union[pygame.Surface,pygame.SurfaceType]:
        return pygame.display.set_mode([width, height], HWSURFACE | DOUBLEBUF | RESIZABLE)

    @staticmethod
    def display_set_caption(text: str):
        pygame.display.set_caption(text)

    @staticmethod
    def mouse_get_pressed() -> Tuple[bool, bool, bool]:
        return pygame.mouse.get_pressed()

    @staticmethod
    def display_flip() -> None:
        pygame.display.flip()

    @staticmethod
    def transform_flip(*args) -> Union[pygame.Surface, pygame.SurfaceType]:
        return pygame.transform.flip(*args)
    @staticmethod
    def clock_init() -> pygame.time.Clock:
        return pygame.time.Clock()

    @staticmethod
    def event_get() -> List[pygame.event.Event]:
        return pygame.event.get()

    @staticmethod
    def rotate(surface: pygame.Surface, alfa: float) -> Union[pygame.Surface, pygame.SurfaceType]:
        return pygame.transform.rotate(surface, alfa)

    @staticmethod
    def scale(pic: pygame.Surface, size: [int, int]) -> Union[pygame.Surface, pygame.SurfaceType]:
        return pygame.transform.scale(pic, size)

    @staticmethod
    def image_load(image_path: str) -> Union[pygame.Surface, pygame.SurfaceType]:
        return pygame.image.load(image_path)

    @staticmethod
    def set_font(font: str, font_size: int, use_freetype: bool = False):
        pygame.font.init()
        if use_freetype is False:
            return pygame.font.SysFont(font, font_size)
        else:
            return pygame.freetype.Font(font,font_size)

    @staticmethod
    def make_event(type: int, data: Any):
        return pygame.event.Event(type, data)

    @staticmethod
    def post_event(event: pygame.event.Event):
        pygame.event.post(event)
