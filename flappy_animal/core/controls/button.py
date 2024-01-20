from flappy_animal.core.wrapper import PyGameWrapper, pygame
from flappy_animal.core.utils import Tuple
from flappy_animal.core.display import Window
class Button(object):
    def __init__(self, name: str, location: Tuple, image: str, window: Window, function, func_args) -> None:
        self.name: str = name
        self.window: Window = window
        self.function = function
        self.func_args = func_args
        self.location: Tuple = location
        self.image: pygame.Surface = PyGameWrapper.image_load("flappy_animal/assets/buttons/" + image)
        self.button_width: int = 0
        self.button_height: int = 0
        self.end_x: int = 0
        self.end_y: int = 0
        self.clicked: bool = False

    def draw(self) -> None:
        self.end_x = self.image.get_width() + self.location[0]
        self.end_y = self.image.get_height() + self.location[1]
        self.window.blit(self.image, self.location)

    def click(self) -> None:
        if self.function is not None and self.func_args is not None:
            self.function(self.func_args)
        elif self.function is not None and self.func_args is None:
            self.function()

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
