from flappy_animal.core.commons import os
from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.game_events import Handler
from flappy_animal.core.utils import Tuple, Union, Any
class Window:
    def __init__(self, width: int, height: int, handler: Handler) -> None:
        self.width: int = width
        self.height: int = height
        self.handler: Handler = handler
        self.surface: pygame.Surface = PyGameWrapper.display_set_mode(self.width, self.height)
        self.ratio: float = width / height
        self.viewport_width: int = self.width
        self.viewport_height: int = self.height
        self.viewport_ratio: float = self.viewport_width / self.viewport_height

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
        PyGameWrapper.update()

    def resize(self, size: int, screen: Any) -> None:
        self.surface = PyGameWrapper.display_set_mode(size[0], size[1])
        for text in screen.text_boxes:
            text.update(location=(size[0]/2-300, text.location[1]))
            text.draw()
        for button in screen.buttons:
            button.update(location=(size[0]/2 - 135, button.location[1]))
            button.draw()
        bg = PyGameWrapper.image_load(os.path.join("flappy_animal/assets/images/backgrounds", screen.background))
        screen.window.blit(PyGameWrapper.scale(bg, size), (0, 0))
    @staticmethod
    def flip() -> None:
        PyGameWrapper.display_flip()

    @staticmethod
    def caption(text) -> None:
        PyGameWrapper.display_set_caption(text)

    def blit(self, surface: pygame.Surface, location: Tuple) -> None:
        self.surface.blit(surface, location)

    def set_background(self, color: Tuple = None, image: str = None) -> Union[pygame.Surface, None]:

        if color is not None:
            self.surface.fill(color)

        elif image is not None:
            bg = PyGameWrapper.image_load(os.path.join("flappy_animal/assets/images/backgrounds", image))
            PyGameWrapper.scale(bg, (self.width, self.height))
            self.surface.blit(bg, (0, 0))
            return bg
